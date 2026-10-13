# pip install chromadb

import chromadb
# import ollama
from sentence_transformers import SentenceTransformer
# chunk_size=5
# overlapping=2
# def get_chunked_docs_li(documents):
#     ids = []
#     chunk_li = []
#     for docs in documents:
        

def get_embedding(documents):
    embed = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = embed.encode(documents, normalize_embeddings=True).tolist()
    return embeddings

def create_collection(collection, embeddings, documents):
    
    for idx, doc in enumerate(documents):
        # Generate vector embeddings using Ollama's embedding model
        # response = ollama.embeddings(model="nomic-embed-text", prompt=doc)
        # embedding = response["embedding"]
        
        # Add the text and its corresponding vector into the database
        collection.add(
            ids=[f"doc_{idx}"],
            embeddings=[embeddings[idx]],
            documents=[doc]
        )

# chroma_client = chromadb.Client()  #In-memory
chroma_client = chromadb.PersistentClient(path="./doc_rag_db")

collection = chroma_client.create_collection(name="my_collection")

documents = [
    "Company policy: Employees can work remotely up to 3 days a week. Core collaborative hours are 10 AM to 3 PM.",
    "Expense guidelines: Daily meal allowance during business trips is capped at $75 USD. Receipts must be uploaded within 15 days.",
    "IT Support: To reset your portal password, use the self-service tool at https://identity.internal or Slack the bot @ITHelper."
]

embeddings = get_embedding(documents)
# print(documents[0])
# print(embeddings[0])
create_collection(collection, embeddings, documents)