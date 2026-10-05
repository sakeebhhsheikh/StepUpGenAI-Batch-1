from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()



################--Direct File Search--##################

# file = client.files.create(
#     file=open("C:\\Users\\HP.DESKTOP-SSLBTGT\\Desktop\\PythonGenAI\\StepUpGenAI-Batch-1\\GenAI\\input_data.txt", "rb"),
#     purpose="user_data"
# )

# prompt = "Does python support object oriented programming ?"

# response = client.responses.create(
#     model="gpt-5.6-sol",
#     input=[
#         {
#             "role" : "user",
#             "content" : [
#                 {
#                     "type" : "input_file",
#                     "file_id" : file.id
#                 },
#                 {
#                     "type" : "input_text",
#                     "text" : prompt
#                 }

#             ]
#         },
#     ],
    
# )

# print(response.output_text)


##########################################################
"""
from openai import OpenAI

client = OpenAI()

# Step 1: Upload the local PDF
pdf_file = client.files.create(
    file=open("report.pdf", "rb"),
    purpose="user_data"
)

print("File ID:", pdf_file.id)

# Step 2: Pass the uploaded PDF to the model
response = client.responses.create(
    model="gpt-5.4",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": pdf_file.id
                },
                {
                    "type": "input_text",
                    "text": "Summarize this PDF."
                }
            ]
        }
    ]
)

print(response.output_text)
"""

# #=========================================================================================
# Use pydantic approach to validate and generate the json output.
# Generate full python code and the required prompt.
# Use both approaches : direct file input and vector store approach.
prompt = """
You are a python AI developer, you have been ask to read the given text file and extract university name, registrar email id and vice chancellor email id if available in data.

Do not assume anything, extract the exact data as appeared in given file.
email id can be from different domains

Input Example section in file : 
Abhilashi University(Private University)
Chailchowk, Tehsil Chachyot, District Mandi 175 028 (HP)
VC Prof AS Guleria (01907)(250015 9418030546)
Reg Major J C Patial (Retd) (250011 9418385090)
E Mail: vicechancellor@abhilalshi.in/regabhilashi@gmail.com
FAX 01907-250407
Example expected outcome For every university the expected list of dict outcome is as follows : 
{"university":"Abhilashi University(Private University)", "address":"Chailchowk, Tehsil Chachyot, District Mandi 175 028 (HP)","vice-chancellor":"Prof AS Guleria", "vice-chancellor-contact":"01907-250015 9418030546", "vice-chancellor-email":"vicechancellor@abhilalshi.in", "registrar":"Major J C Patial", "registrar-contact":"250011 9418385090" "registrar-email":"regabhilashi@gmail.com" }

"""


####################################################################################
# https://developers.openai.com/api/docs/guides/file-inputs?utm_source=chatgpt.com&api-mode=responses

"""from openai import OpenAI

client = OpenAI()

input_file_path = "C:\\Users\\HP.DESKTOP-SSLBTGT\\Desktop\\PythonGenAI\\StepUpGenAI-Batch-1\\GenAI\\Task-1\\output.txt"

# Step 1: Upload the local PDF
email_data_file = client.files.create(
    file=open(input_file_path, "rb"),
    purpose="user_data"
)

print("File ID:", email_data_file.id)

# Step 2: Pass the uploaded PDF to the model
response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": email_data_file.id
                },
                {
                    "type": "input_text",
                    "text": prompt
                }
            ]
        }
    ]
)

print(response.output_text)"""


##############################################################################
##############################################################################
# Using Vector store

# --------------------------------------------------
# 2. Create Vector Store
# --------------------------------------------------

"""vector_store = client.vector_stores.create(
    name="University Documents"
)

print("Vector Store ID:", vector_store.id)

# --------------------------------------------------
# 3. Upload PDF + attach to Vector Store
#    + wait until indexing finishes
# --------------------------------------------------

input_file_path = r"C:\Users\HP.DESKTOP-SSLBTGT\Desktop\PythonGenAI\StepUpGenAI-Batch-1\GenAI\Task-1\output.txt"

with open(input_file_path, "rb") as pdf_file:

    vector_store_file = client.vector_stores.files.upload_and_poll(
        vector_store_id=vector_store.id,
        file=pdf_file,
    )

print("File status:", vector_store_file.status)

if vector_store_file.status != "completed":
    raise RuntimeError(
        f"File indexing failed: {vector_store_file.last_error}"
    )


# Step 1: Upload the local PDF
# email_data_file = client.files.create(
#     file=open(r"C:\Users\HP.DESKTOP-SSLBTGT\Desktop\PythonGenAI\StepUpGenAI-Batch-1\GenAI\Task-1\output.txt", "rb"),
#     purpose="user_data"
# )

# print("File ID:", email_data_file.id)

# Step 2: Pass the uploaded PDF to the model
response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": prompt
                }
            ]
        }
    ],
    tools=[
        {
            "type": "file_search",
            "vector_store_ids": [
                vector_store.id
            ],
            "max_num_results": 10
        }
    ]
)

print(response.output_text)"""


#######################################################################################
import os
import json
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field


# ============================================================
# 1. CONFIGURATION
# ============================================================

load_dotenv()

client = OpenAI()

MODEL = os.getenv("OPENAI_MODEL", "YOUR_MODEL_ID")

FILE_PATH = r"C:\Users\HP.DESKTOP-SSLBTGT\Desktop\PythonGenAI\StepUpGenAI-Batch-1\GenAI\Task-1\output.txt"


# ============================================================
# 2. PYDANTIC MODEL
# ============================================================

class UniversityRecord(BaseModel):

    university: str = Field(
        description="Exact university name as written in the source document."
    )

    address: Optional[str] = Field(
        default=None,
        description="Exact university address from the source document."
    )

    vice_chancellor: Optional[str] = Field(
        default=None,
        description="Exact Vice Chancellor name from the source document."
    )

    registrar: Optional[str] = Field(
        default=None,
        description="Exact Registrar name from the source document."
    )

    vice_chancellor_email: Optional[str] = Field(
        default=None,
        description="Vice Chancellor email if explicitly available."
    )

    registrar_email: Optional[str] = Field(
        default=None,
        description="Registrar email if explicitly available."
    )


# ============================================================
# 3. CREATE VECTOR STORE
# ============================================================

vector_store = client.vector_stores.create(
    name="University Directory"
)

print("Vector Store ID:", vector_store.id)


# ============================================================
# 4. UPLOAD PDF AND WAIT FOR INDEXING
# ============================================================

with open(FILE_PATH, "rb") as pdf:

    vector_file = client.vector_stores.files.upload_and_poll(
        vector_store_id=vector_store.id,
        file=pdf
    )


print("Indexing status:", vector_file.status)

if vector_file.status != "completed":
    raise RuntimeError(
        f"Indexing failed: {vector_file.last_error}"
    )


# ============================================================
# 5. FILE SEARCH + PYDANTIC STRUCTURED OUTPUT
# ============================================================

university_name = "Abhilashi University"

prompt = f"""
Search the supplied university directory for:

{university_name}

Extract ONLY information explicitly present in the source document.

Rules:

1. Do not guess or infer missing information.

2. Preserve the university name exactly as written.

3. Preserve the address exactly as written.

4. Extract the Vice Chancellor name only if explicitly available.

5. Extract the Registrar name only if explicitly available.

6. Extract the Vice Chancellor email only when the document clearly
   associates the email with the Vice Chancellor.

7. Extract the Registrar email only when the document clearly
   associates the email with the Registrar.

8. Email addresses may use any domain, including Gmail.

9. If a field is unavailable or cannot be reliably determined,
   return null.

10. Do not invent information.
"""


response = client.responses.parse(

    model=MODEL,

    input=prompt,

    tools=[
        {
            "type": "file_search",

            "vector_store_ids": [
                vector_store.id
            ],

            "max_num_results": 10
        }
    ],

    text_format=UniversityRecord,

    # Very useful while developing:
    include=[
        "file_search_call.results"
    ]
)


# ============================================================
# 6. GET VALIDATED PYDANTIC OBJECT
# ============================================================

university = response.output_parsed

if university is None:
    raise RuntimeError(
        "The model did not return a valid UniversityRecord."
    )


# ============================================================
# 7. ACCESS FIELDS AS NORMAL PYTHON
# ============================================================

print("\n--- PYDANTIC OBJECT ---")

print("University:", university.university)
print("Address:", university.address)
print("Vice Chancellor:", university.vice_chancellor)
print("Registrar:", university.registrar)
print(
    "Vice Chancellor Email:",
    university.vice_chancellor_email
)
print(
    "Registrar Email:",
    university.registrar_email
)


# ============================================================
# 8. CONVERT PYDANTIC -> DICTIONARY
# ============================================================

record = university.model_dump()

print("\n--- PYTHON DICTIONARY ---")

print(record)


# ============================================================
# 9. CONVERT PYDANTIC -> JSON
# ============================================================

print("\n--- JSON ---")

print(
    university.model_dump_json(indent=2)
)


# ============================================================
# 10. SAVE JSON
# ============================================================

with open(
    "university_result.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        record,
        f,
        indent=2,
        ensure_ascii=False
    )


print("\nSaved to university_result.json")