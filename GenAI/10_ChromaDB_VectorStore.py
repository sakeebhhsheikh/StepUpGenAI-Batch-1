#==> Step 1: Install Required Libraries
# pip install ollama chromadb

#==> Step 2: Download Your Models
#- you need two types of models:
    # 1. Embedding Model to turn text chunks into mathematical vectors (numbers) for searching.
    # 2. A Generation Model (LLM) to read the text and write a smart answer.

    #-> Download a highly efficient text embedding model
    # ollama pull nomic-embed-text

    #-> Download a compact, high-quality generation model
    # ollama pull llama3

#==> Step 3: Write the Complete RAG Script

import ollama
import chromadb

# 1. Initialize the local persistent Vector Database
# This creates a folder named 'rag_db' in your directory to store your document memory
chroma_client = chromadb.PersistentClient(path="./rag_db")

# Create or fetch a collection (think of it as a table in a database)
collection = chroma_client.get_or_create_collection(name="private_knowledge")

# 2. Your custom documents/knowledge base
# Replace these with real data or logic to read raw txt/PDF files
documents = [
    "Company policy: Employees can work remotely up to 3 days a week. Core collaborative hours are 10 AM to 3 PM.",
    "Expense guidelines: Daily meal allowance during business trips is capped at $75 USD. Receipts must be uploaded within 15 days.",
    "IT Support: To reset your portal password, use the self-service tool at https://identity.internal or Slack the bot @ITHelper."
]


# 3. Ingestion: Embed and store documents
for idx, doc in enumerate(documents):
    # Generate vector embeddings using Ollama's embedding model
    response = ollama.embeddings(model="nomic-embed-text", prompt=doc)
    embedding = response["embedding"]
    
    # Add the text and its corresponding vector into the database
    collection.upsert(
        ids=[f"doc_{idx}"],
        embeddings=[embedding],
        documents=[doc]
    )

print("Indexing complete!\n")

# 4. Retrieval: Define the User Query and search the database
user_query = "What is the maximum budget allowed for food when traveling for work?"
print(f"User Query: '{user_query}'")

# Generate an embedding for the user's question
query_emb_response = ollama.embeddings(model="nomic-embed-text", prompt=user_query)
query_embedding = query_emb_response["embedding"]

# Query the database for the top 1 closest matching document chunk (n_results=1)
search_results = collection.query(
    query_embeddings=[query_embedding],
    n_results=1
)

# Extract the matching text chunk
retrieved_context = search_results["documents"][0][0]
print(f"Retrieved Context from DB: '{retrieved_context}'\n")

# 5. Generation: Construct the augmented prompt and query the LLM
augmented_prompt = f"""
You are a helpful company assistant. Use ONLY the following pieces of context to answer the question at the end. If you don't know the answer, say that you don't know.

Context:
{retrieved_context}

Question: {user_query}
Answer:
"""

print("Generating final answer via Ollama (Llama3)...")
output = ollama.chat(
    model="llama3",
    messages=[{"role": "user", "content": augmented_prompt}]
)

print("\n--- FINAL LLM RESPONSE ---")
print(output["message"]["content"])