# pip install --upgrade transformers

# pip install -U transformers datasets evaluate accelerate torch

"""
import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    api_key=os.environ["HF_TOKEN"]
)

messages = [
    {
        "role": "system",
        "content": "You are a pirate chatbot who always responds in pirate speak!"
    },
    {
        "role": "user",
        "content": "Who are you?"
    }
]

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct",
    messages=messages,
    max_tokens=256
)

print(response.choices[0].message.content)
"""

## ==> Run Local Model using Pipeline for Sentiment Analysis: 

# from transformers import pipeline

# # Load a pretrained sentiment-analysis model
# classifier = pipeline(
#     "sentiment-analysis",
#     model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
# )

# texts = [
#     "Hugging Face makes AI development easier.",
#     "The application is slow and difficult to use.",
#     "The product is excellent, but delivery was late."
# ]

# results = classifier(texts)

# for text, result in zip(texts, results):
#     print("Text:", text)
#     print("Sentiment:", result["label"])
#     print("Confidence:", round(result["score"], 4))
#     print("-" * 40)


#==> what happens behind the simple pipeline

"""
from transformers import AutoTokenizer

model_name = "distilbert/distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)

text = "Hugging Face makes natural language processing easier."

tokens = tokenizer.tokenize(text)
encoded = tokenizer(text)

print("Tokens:", tokens)
print("Token IDs:", encoded["input_ids"])
print("Attention mask:", encoded["attention_mask"])

print("Decoded text:", tokenizer.decode(encoded["input_ids"]))
"""
#####################################################################

"""
import torch
from transformers import AutoTokenizer, AutoModel

model_name = "distilbert/distilbert-base-uncased"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

inputs = tokenizer(
    "Transformers convert text into contextual representations.",
    return_tensors="pt"
)

with torch.no_grad():
    outputs = model(**inputs)

print("Input shape:", inputs["input_ids"].shape)
print("Hidden state shape:", outputs.last_hidden_state.shape)
print("Decoded text:", tokenizer.decode(inputs["input_ids"]))

"""

"""
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load API key from .env
load_dotenv()


client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

messages = [
    {
        "role": "system",
        "content": "You are a pirate chatbot who always responds in pirate speak!"
    },
    {
        "role": "user",
        "content": "Who are you?"
    }
]

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-7B-Instruct-1M",
    messages=messages,
    max_tokens=256
)

print(response.choices[0].message.content)
"""

#####################################################
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

prompt = "What is the currency of India?"

model_id = "gpt3.5"
api_url = f"https://api-inference.huggingface.co/models/{model_id}"

header = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}
payload = {"inputs": prompt, "parameters": {"max_new_tokens": 200}}

response = requests.post(api_url, headers=header, json=payload)
response.raise_for_status()

data = response.json()
print(data[0]["generated_text"].strip())"""



"""import os
from dotenv import load_dotenv

load_dotenv()
from huggingface_hub import InferenceClient

# Initialize the client with your free token
client = InferenceClient(provider="hf-inference", token=os.getenv('HF_TOKEN'))

# Call an open-source model (like Mistral, Llama, etc.)
response = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.3", 
    messages=[{"role": "user", "content": "Explain quantum computing in one sentence."}],
    max_tokens=500,
)

print(response.choices[0].message.content)"""


# import os
# from dotenv import load_dotenv

# load_dotenv()
# from huggingface_hub import InferenceClient

# # No explicit provider needed; it routes automatically
# client = InferenceClient(token=os.getenv('HF_TOKEN'))

# response = client.chat.completions.create(
#     model="meta-llama/Llama-3.1-8B-Instruct", 
#     messages=[{"role": "user", "content": "Explain quantum computing in one sentence."}],
#     max_tokens=500,
# )

# print(response.choices[0].message.content)


# import os
# from huggingface_hub import InferenceClient

# client = InferenceClient(
#     provider="auto",
#     api_key=os.environ["HF_TOKEN"],
# )

# # output is a PIL.Image object
# image = client.text_to_image(
#     "Astronaut riding a horse",
#     model="black-forest-labs/FLUX.1-schnell",
# )

# ============================================================

# from transformers import pipeline
# import torch

# pipe = pipeline("text-generation", 
#                 model="google/gemma-3-1b-it", 
#                 device="cuda", 
#                 torch_dtype=torch.bfloat16)

# messages = [
#     [
#         {
#             "role": "system",
#             "content": [{"type": "text", "text": "You are a helpful assistant."},]
#         },
#         {
#             "role": "user",
#             "content": [{"type": "text", "text": "Write a poem on Hugging Face, the company"},]
#         },
#     ],
# ]

# output = pipe(messages, max_new_tokens=50)
# print(output)

from transformers import GPT2Tokenizer, GPT2Model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2Model.from_pretrained('gpt2')
text = "Replace me by any text you'd like."
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
print(output)