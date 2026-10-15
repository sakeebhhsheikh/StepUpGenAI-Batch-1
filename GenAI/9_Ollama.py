# Types of models : 
# 1. Text Generation models : llama3, mistral, gemma2
# 2. Code Generation : codellama, deepseek-coder
# 3. Embedding models : nomic-embed-text, embeddinggemma
# 4. Lightweight / Efficient models : phi3, qwen2

# ollama run llama3:latest
# ollama stop llama3
# ollama stop llama3:latest

#-> View All Downloaded Models
# ollama list
#-> Remove a Model
# ollama rm <model_name>



import ollama

model_name = "llama3"

prompt = "Write a short bed time story of 5 lines for my daughter."

response = ollama.chat(
    model=model_name,
    messages = [
        {
            "role" : "user",
            "content" : prompt
        },
    ],
    stream=True,
)

# print("Response :::")
# print(response['message']['content'])
# print("##"*10)
# print(response)

for chunk in response:
    print(chunk["message"]["content"], end="", flush=True)
print() 

#==> Ollama --> load and run llm models, text embedding
#==> ChromaDB --> to store vectors
#==> LangChain --> Framework
#==> Pydandic --> structure output and output validation

#==> Langgraph, Neo4j, Langfuse, Streamlit, Langsmith

#==> Fine Tune models : 

