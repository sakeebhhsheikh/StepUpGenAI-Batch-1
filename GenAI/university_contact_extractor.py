#!/usr/bin/env python3
"""Extract university contacts from a source file with the OpenAI Responses API.

Two modes are supported:
  1. direct: upload the file and pass it directly as an input_file.
  2. vector: upload the file, index it in a vector store, and use file_search.

The model response is constrained and validated by Pydantic before JSON is saved.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path
from openai import OpenAI
from pydantic import BaseModel, ConfigDict, Field, field_validator


MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")

EXTRACTION_PROMPT = r"""
You are a precise data-extraction system. Extract EVERY university record from
the supplied source file. The records are normally separated by a line of #
characters.

NON-NEGOTIABLE RULES
1. Use only text present in the source. Never guess, complete, correct, or look
   up a name, address, telephone number, or email address.
2. Preserve source spelling, capitalization, punctuation, and OCR errors in
   extracted values. Do not repair a suspicious email or truncated word.
3. Return one record for every university block, in source order. Do not merge
   neighboring blocks and do not omit a block because some fields are missing.
4. Use null when a field is absent, illegible, truncated before any usable
   value, or cannot be assigned to that field unambiguously. Never use an empty
   string, "N/A", "unknown", or an invented value.
5. "VC" identifies the vice-chancellor line; "Reg" identifies the registrar
   line. Remove those role labels from the corresponding person's name.
   Keep printed titles such as Prof, Dr, Shri, or Major. Exclude a retirement
   status such as "(Retd)" from the person's name.
6. For contacts, copy only the number groups printed on that person's VC or Reg
   line. Do not take EPABX or FAX numbers. When an area code and local number are
   printed in adjacent parentheses, render them as area-code-local-number, then
   preserve any separately printed mobile number after one space. Do not infer
   missing digits or closing parentheses.
7. An email can use any domain, including gmail.com or yahoo.com. Do not reject
   an email merely because it is not on the university's domain.
8. On a shared email line containing two slash-separated addresses, assign the
   first address to the vice-chancellor and the second to the registrar only
   when the block presents them in VC-then-Reg order. If only one email is
   printed and its owner is not explicitly or structurally unambiguous, leave
   the uncertain role email null.
9. Strip only surrounding whitespace and extraction labels (for example,
   "E Mail:"). Do not otherwise rewrite extracted text.

FIELD MEANINGS
- university: the university heading, including the printed parenthetical
  university type when present.
- address: address/location text belonging to that block, excluding staff,
  email, EPABX, and FAX lines.
- vice-chancellor / registrar: the printed person's name without the VC/Reg
  label or telephone groups.
- *-contact: contact number groups from that person's own line only.
- *-email: the syntactically complete email address assigned by the rules.

REFERENCE EXAMPLE
Source:
Abhilashi University(Private University)
Chailchowk, Tehsil Chachyot, District Mandi 175 028 (HP)
VC Prof AS Guleria (01907)(250015 9418030546)
Reg Major J C Patial (Retd) (250011 9418385090)
E Mail: vicechancellor@abhilalshi.in/regabhilashi@gmail.com

Expected record:
{
  "university": "Abhilashi University(Private University)",
  "address": "Chailchowk, Tehsil Chachyot, District Mandi 175 028 (HP)",
  "vice-chancellor": "Prof AS Guleria",
  "vice-chancellor-contact": "01907-250015 9418030546",
  "vice-chancellor-email": "vicechancellor@abhilalshi.in",
  "registrar": "Major J C Patial",
  "registrar-contact": "250011 9418385090",
  "registrar-email": "regabhilashi@gmail.com"
}
""".strip()


EMAIL_PATTERN = re.compile(r"^[^\s@/]+@[^\s@/]+\.[^\s@/]+$")


class UniversityRecord(BaseModel):
    """One validated university record, serialized with requested JSON keys."""

    model_config = ConfigDict(extra="forbid", strict=True, populate_by_name=True)

    university: str = Field(min_length=1)
    address: str | None = None
    vice_chancellor: str | None = Field(default=None, alias="vice-chancellor")
    vice_chancellor_contact: str | None = Field(
        default=None, alias="vice-chancellor-contact"
    )
    vice_chancellor_email: str | None = Field(
        default=None, alias="vice-chancellor-email"
    )
    registrar: str | None = None
    registrar_contact: str | None = Field(default=None, alias="registrar-contact")
    registrar_email: str | None = Field(default=None, alias="registrar-email")

    @field_validator("vice_chancellor_email", "registrar_email")
    @classmethod
    def validate_email_without_rewriting(cls, value: str | None) -> str | None:
        """Validate basic email syntax while returning the exact input string."""
        if value is not None and not EMAIL_PATTERN.fullmatch(value):
            raise ValueError("must be one complete email address with no whitespace")
        return value

    @field_validator(
        "address",
        "vice_chancellor",
        "vice_chancellor_contact",
        "registrar",
        "registrar_contact",
    )
    @classmethod
    def reject_blank_optional_strings(cls, value: str | None) -> str | None:
        if value is not None and not value.strip():
            raise ValueError("use null instead of a blank string")
        return value


class ExtractionResult(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    universities: list[UniversityRecord]


def parsed_result(response: object) -> ExtractionResult:
    result = getattr(response, "output_parsed", None)
    if result is None:
        output_text = getattr(response, "output_text", "")
        raise RuntimeError(
            "The API returned no parsed object. Raw output was: " + repr(output_text)
        )
    # responses.parse normally returns the Pydantic instance. Re-validating is
    # intentional: it protects this code if an SDK version returns plain data.
    return ExtractionResult.model_validate(result)


def extract_direct(client: OpenAI, source: Path, model: str) -> ExtractionResult:
    uploaded = client.files.create(file=source, purpose="user_data")
    try:
        response = client.responses.parse(
            model=model,
            input=[
                {"role": "system", "content": EXTRACTION_PROMPT},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "Extract every university record from this file.",
                        },
                        {"type": "input_file", "file_id": uploaded.id},
                    ],
                },
            ],
            text_format=ExtractionResult,
        )
        return parsed_result(response)
    finally:
        client.files.delete(uploaded.id)


def wait_for_vector_file(
    client: OpenAI,
    vector_store_id: str,
    vector_file_id: str,
    timeout_seconds: int = 300,
) -> None:
    deadline = time.monotonic() + timeout_seconds
    while time.monotonic() < deadline:
        page = client.vector_stores.files.list(vector_store_id=vector_store_id)
        item = next((x for x in page.data if x.id == vector_file_id), None)
        if item is not None:
            if item.status == "completed":
                return
            if item.status in {"failed", "cancelled"}:
                raise RuntimeError(
                    f"Vector-store indexing ended with status {item.status!r}."
                )
        time.sleep(2)
    raise TimeoutError("Timed out while waiting for vector-store indexing.")


def extract_vector_store(
    client: OpenAI, source: Path, model: str, keep_remote: bool
) -> ExtractionResult:
    uploaded = client.files.create(file=source, purpose="user_data")
    vector_store = client.vector_stores.create(
        name=f"university-contact-extraction-{source.stem}"
    )
    try:
        vector_file = client.vector_stores.files.create(
            vector_store_id=vector_store.id,
            file_id=uploaded.id,
        )
        wait_for_vector_file(client, vector_store.id, vector_file.id)

        response = client.responses.parse(
            model=model,
            input=[
                {"role": "system", "content": EXTRACTION_PROMPT},
                {
                    "role": "user",
                    "content": (
                        "Search the indexed source file and extract every university "
                        "record. Ensure all source blocks are represented exactly once."
                    ),
                },
            ],
            tools=[
                {
                    "type": "file_search",
                    "vector_store_ids": [vector_store.id],
                    "max_num_results": 50,
                }
            ],
            text_format=ExtractionResult,
        )
        return parsed_result(response)
    finally:
        if keep_remote:
            print(
                f"Kept file_id={uploaded.id} and vector_store_id={vector_store.id}"
            )
        else:
            # Only resources created by this invocation are removed.
            client.vector_stores.delete(vector_store.id)
            client.files.delete(uploaded.id)


def save_json(result: ExtractionResult, destination: Path) -> None:
    records = [
        item.model_dump(mode="json", by_alias=True)
        for item in result.universities
    ]
    destination.write_text(
        json.dumps(records, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract validated university contact records into JSON."
    )
    parser.add_argument("input_file", type=Path)
    parser.add_argument(
        "--approach",
        choices=("direct", "vector"),
        required=True,
        help="Pass the file directly or retrieve it through a vector store.",
    )
    parser.add_argument("--output", type=Path, default=Path("universities.json"))
    parser.add_argument("--model", default=MODEL)
    parser.add_argument(
        "--keep-remote",
        action="store_true",
        help="Keep the newly uploaded file/vector store instead of cleaning it up.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = args.input_file.expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(f"Input file does not exist: {source}")
    if not os.getenv("OPENAI_API_KEY"):
        raise EnvironmentError("Set the OPENAI_API_KEY environment variable first.")

    client = OpenAI()
    if args.approach == "direct":
        result = extract_direct(client, source, args.model)
    else:
        result = extract_vector_store(
            client, source, args.model, keep_remote=args.keep_remote
        )

    save_json(result, args.output)
    print(f"Saved {len(result.universities)} records to {args.output}")


if __name__ == "__main__":
    main()
