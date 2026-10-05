from openai import OpenAI
import os
from dotenv import load_dotenv

# OPENAI_API_KEY --> Standard name for OPENAI api key
# Load API key from .env
load_dotenv()

client = OpenAI()

stream = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": "Say 'double bubble bath' ten times fast.",
        },
    ],
    stream=True
)

for event in stream:
    print(event)

   