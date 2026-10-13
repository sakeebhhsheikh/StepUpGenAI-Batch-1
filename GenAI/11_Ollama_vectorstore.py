import os
import ollama
import chromadb
from pypdf import PdfReader

# 1. Initialize Vector Database
chroma_client = chromadb.PersistentClient(path="./rag_db")
collection = chroma_client.get_or_create_collection(name="file_knowledge")

# 2. Functions to load actual files from your computer
def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def read_pdf_file(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

# 3. Simple function to split long text into smaller chunks
def split_into_chunks(text, chunk_size=500):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    
    for word in words:
        current_chunk.append(word)
        current_length += len(word) + 1 # +1 for the space
        if current_length >= chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0
            
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

# --- CONFIGURATION: Specify your file paths here ---
# Change these paths to files on your computer!
FILE_PATH = "document.pdf"  # target PDF or change to "sample.txt"

print(f"Reading file: {FILE_PATH}...")

# Load the file based on its extension
if FILE_PATH.endswith(".pdf"):
    raw_text = read_pdf_file(FILE_PATH)
elif FILE_PATH.endswith(".txt"):
    raw_text = read_text_file(FILE_PATH)
else:
    raise ValueError("Unsupported file format. Please use .pdf or .txt")

# Break the file down into search-friendly pieces
document_chunks = split_into_chunks(raw_text, chunk_size=400)
print(f"Split document into {len(document_chunks)} chunks.")

# 4. Ingestion: Embed chunks into ChromaDB
print("Indexing chunks into ChromaDB...")
for idx, chunk in enumerate(document_chunks):
    # Only index non-empty chunks
    if not chunk.strip():
        continue
        
    response = ollama.embeddings(model="nomic-embed-text", prompt=chunk)
    embedding = response["embedding"]
    
    # Generate unique ID for each chunk based on filename and index
    file_id = f"{os.path.basename(FILE_PATH)}_chunk_{idx}"
    
    collection.upsert(
        ids=[file_id],
        embeddings=[embedding],
        documents=[chunk]
    )
print("Database successfully updated!\n")

# 5. Ask a question about your uploaded file
user_query = "What are the key conclusions or summaries mentioned in this file?" 
print(f"User Query: '{user_query}'")

# Generate query embedding
query_emb_response = ollama.embeddings(model="nomic-embed-text", prompt=user_query)
query_embedding = query_emb_response["embedding"]

# Retrieve the top 2 most relevant chunks from the document
search_results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)
retrieved_context = "\n\n".join(search_results["documents"][0])

# 6. Generate final answer grounding it in your file's data
augmented_prompt = f"""
You are a helpful assistant reading a custom document. Use the provided context below to answer the user's question accurately.

Context:
{retrieved_context}

Question: {user_query}
Answer:
"""

print("Generating response via Llama3...")
output = ollama.chat(
    model="llama3",
    messages=[{"role": "user", "content": augmented_prompt}]
)

print("\n--- LLM RESPONSE FROM YOUR FILE ---")
print(output["message"]["content"])


# python file_rag.py