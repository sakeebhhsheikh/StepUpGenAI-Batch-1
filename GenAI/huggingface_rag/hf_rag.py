
# rag_app.py

import argparse
import re
from typing import Any, Dict, List, Optional

import faiss
import numpy as np
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from transformers import pipeline


# ---------------------------------------------------------
# 1. Configuration
# ---------------------------------------------------------

DATASET_NAME = "rag-datasets/rag-mini-wikipedia"
DATASET_CONFIG = "text-corpus"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
# GENERATION_MODEL = "google/flan-t5-base"
# GENERATION_MODEL = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
GENERATION_MODEL = "Qwen/Qwen2.5-1.5B-Instruct"

CHUNK_SIZE = 120       # Approximate number of words
CHUNK_OVERLAP = 25     # Words shared between adjacent chunks
TOP_K = 3              # Number of passages retrieved


# ---------------------------------------------------------
# 2. Extract text from the dataset
# ---------------------------------------------------------

def extract_passages(dataset_split) -> List[str]:
    """
    Extract document text from a Hugging Face Dataset split.

    Supports common text-column names and falls back to
    inspecting the values in the first row.
    """
    if len(dataset_split) == 0:
        return []

    columns = dataset_split.column_names

    preferred_columns = [
        "passage",
        "text",
        "content",
        "document",
        "document_text",
        "context",
    ]

    text_column = next(
        (
            col for col in preferred_columns
            if col in columns
        ),
        None,
    )

    # Fallback for datasets with a different column name.
    if text_column is None:
        first_row = dataset_split[0]

        candidates = [
            (key, value)
            for key, value in first_row.items()
            if isinstance(value, str) and value.strip()
        ]

        if not candidates:
            raise ValueError(
                f"No text column found. Available columns: {columns}"
            )

        # Select the longest string value as a heuristic.
        text_column = max(
            candidates,
            key=lambda item: len(item[1]),
        )[0]

    passages = []

    for row in dataset_split:
        value = row.get(text_column)

        if isinstance(value, str):
            value = re.sub(r"\s+", " ", value).strip()

            if value:
                passages.append(value)

    return passages


def load_wikipedia_passages(
    dataset_name: str = DATASET_NAME,
    config_name: str = DATASET_CONFIG,
    max_documents: Optional[int] = None,
) -> List[str]:
    """
    Load the Wikipedia text corpus.

    max_documents is useful for development and testing.
    None means load all documents from the selected split.
    """
    dataset = load_dataset(dataset_name, config_name)

    # The corpus config normally exposes a 'passages' split.
    if "passages" in dataset:
        split = dataset["passages"]
    else:
        # Handle a dataset that exposes a different split name.
        split = dataset[next(iter(dataset.keys()))]

    if max_documents is not None:
        if max_documents < 1:
            raise ValueError("max_documents must be positive.")

        split = split.select(
            range(min(max_documents, len(split)))
        )

    passages = extract_passages(split)

    if not passages:
        raise ValueError("The dataset contains no usable text.")

    print(f"Loaded {len(passages)} Wikipedia documents.")

    return passages


# ---------------------------------------------------------
# 3. Split documents into overlapping chunks
# ---------------------------------------------------------

def chunk_text(
    text: str,
    chunk_size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP,
) -> List[str]:
    """
    Split text into word-based chunks.

    Example:
        chunk_size = 100
        overlap = 20

    The next chunk begins 80 words after the previous
    chunk's starting position.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError(
            "overlap must be >= 0 and smaller than chunk_size."
        )

    words = text.split()

    if not words:
        return []

    step = chunk_size - overlap

    chunks = []

    for start in range(0, len(words), step):
        chunk = " ".join(words[start:start + chunk_size])

        if chunk:
            chunks.append(chunk)

        if start + chunk_size >= len(words):
            break

    return chunks


def build_chunks(
    documents: List[str],
    chunk_size: int = CHUNK_SIZE,
    overlap: int = CHUNK_OVERLAP,
) -> List[Dict[str, Any]]:
    """
    Chunk every document and preserve source metadata.
    """
    all_chunks = []

    for document_id, document in enumerate(documents):
        chunks = chunk_text(
            document,
            chunk_size=chunk_size,
            overlap=overlap,
        )

        for chunk_id, chunk in enumerate(chunks):
            all_chunks.append(
                {
                    "document_id": document_id,
                    "chunk_id": chunk_id,
                    "text": chunk,
                }
            )

    return all_chunks


# ---------------------------------------------------------
# 4. RAG application
# ---------------------------------------------------------

class RAGApplication:
    def __init__(
        self,
        embedding_model=None,
        generator=None,
        top_k: int = TOP_K,
    ):
        if top_k < 1:
            raise ValueError("top_k must be positive.")

        self.embedding_model = embedding_model
        self.generator = generator
        self.top_k = top_k

        self.chunks: List[Dict[str, Any]] = []
        self.index = None

    def build_index(
        self,
        documents: List[str],
        chunk_size: int = CHUNK_SIZE,
        overlap: int = CHUNK_OVERLAP,
        batch_size: int = 64,
    ):
        """
        Create embeddings for all chunks and index them
        with FAISS using cosine similarity.
        """
        if not documents:
            raise ValueError("documents cannot be empty.")

        if batch_size < 1:
            raise ValueError("batch_size must be positive.")

        if self.embedding_model is None:
            self.embedding_model = SentenceTransformer(
                EMBEDDING_MODEL
            )

        self.chunks = build_chunks(
            documents,
            chunk_size=chunk_size,
            overlap=overlap,
        )

        if not self.chunks:
            raise ValueError("No chunks were generated.")

        texts = [chunk["text"] for chunk in self.chunks]

        vectors = self.embedding_model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        vectors = np.asarray(vectors, dtype=np.float32)

        if vectors.ndim != 2 or vectors.shape[0] != len(texts):
            raise ValueError("Embedding model returned invalid vectors.")

        if not np.isfinite(vectors).all():
            raise ValueError("Embeddings contain invalid numeric values.")

        # Normalized vectors + inner product = cosine similarity.
        self.index = faiss.IndexFlatIP(vectors.shape[1])
        self.index.add(np.ascontiguousarray(vectors))

        print(f"Created {len(self.chunks)} text chunks.")
        print(f"FAISS index contains {self.index.ntotal} vectors.")

    # -----------------------------------------------------
    # 5. Retrieve relevant passages
    # -----------------------------------------------------

    def retrieve(
        self,
        question: str,
        top_k: Optional[int] = None,
    ) -> List[Dict[str, Any]]:
        if not question or not question.strip():
            raise ValueError("Question cannot be empty.")

        if self.index is None:
            raise RuntimeError("Build the index before retrieval.")

        if self.embedding_model is None:
            raise RuntimeError("Embedding model is not initialized.")

        k = self.top_k if top_k is None else top_k

        if k < 1:
            raise ValueError("top_k must be positive.")

        k = min(k, self.index.ntotal)

        query_vector = self.embedding_model.encode(
            [question.strip()],
            convert_to_numpy=True,
            normalize_embeddings=True,
        )

        query_vector = np.asarray(
            query_vector,
            dtype=np.float32,
        )

        scores, indices = self.index.search(query_vector, k)

        results = []

        for score, chunk_index in zip(scores[0], indices[0]):
            if chunk_index < 0:
                continue

            result = dict(self.chunks[int(chunk_index)])
            result["score"] = float(score)
            results.append(result)

        return results

    # -----------------------------------------------------
    # 6. Generate an answer using Hugging Face pipeline
    # -----------------------------------------------------

    def load_generator(self):
        if self.generator is None:
            self.generator = pipeline(
                task="text-generation",
                model=GENERATION_MODEL,
                tokenizer=GENERATION_MODEL,
            )

        return self.generator

    def answer(
        self,
        question: str,
        top_k: Optional[int] = None,
        max_new_tokens: int = 128,
    ) -> Dict[str, Any]:
        """
        Retrieve context, generate an answer and return
        the retrieved sources with similarity scores.
        """
        if not question or not question.strip():
            raise ValueError("Question cannot be empty.")

        if max_new_tokens < 1:
            raise ValueError("max_new_tokens must be positive.")

        retrieved = self.retrieve(question, top_k=top_k)

        if not retrieved:
            return {
                "question": question,
                "answer": "I could not find relevant context.",
                "sources": [],
            }

        context = "\n\n".join(
            f"[Source {i + 1}] {item['text']}"
            for i, item in enumerate(retrieved)
        )

        prompt = f"""
Answer the question using only the context below.
If the context does not contain the answer, say:
"I don't know based on the provided context."

Do not invent facts.

Context:
{context}

Question: {question}

Answer:
""".strip()

        generator = self.load_generator()

        generated = generator(
            prompt,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            return_full_text=False,
        )

        answer_text = generated[0]["generated_text"].strip()

        return {
            "question": question,
            "answer": answer_text,
            "sources": retrieved,
        }


# ---------------------------------------------------------
# 7. Command-line application
# ---------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Hugging Face Wikipedia RAG application"
    )

    parser.add_argument(
        "--max-documents",
        type=int,
        default=None,
        help="Optional limit for development.",
    )

    parser.add_argument(
        "--question",
        type=str,
        default=None,
        help="Ask a single question and exit.",
    )

    parser.add_argument(
        "--top-k",
        type=int,
        default=TOP_K,
        help="Number of passages to retrieve.",
    )

    args = parser.parse_args()

    if args.top_k < 1:
        parser.error("--top-k must be positive.")

    documents = load_wikipedia_passages(
        max_documents=args.max_documents
    )

    rag = RAGApplication(top_k=args.top_k)

    rag.build_index(documents)

    if args.question:
        questions = [args.question]
    else:
        questions = None

    while True:
        if questions:
            question = questions.pop(0)
        else:
            try:
                question = input(
                    "\nEnter a question (or 'exit' to quit): "
                ).strip()
            except (EOFError, KeyboardInterrupt):
                print("\nExiting RAG application.")
                break

        if question.lower() in {"exit", "quit"}:
            break

        if not question:
            continue

        try:
            result = rag.answer(question)

            print("\nAnswer:")
            print(result["answer"])

            print("\nRetrieved sources:")

            for i, source in enumerate(result["sources"], start=1):
                print(
                    f"\n{i}. Document {source['document_id']}, "
                    f"Chunk {source['chunk_id']}, "
                    f"Score: {source['score']:.4f}"
                )
                print(source["text"][:500])

        except Exception as exc:
            print(f"Error answering question: {exc}")

        if args.question:
            break


if __name__ == "__main__":
    main()
