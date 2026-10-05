# OPENAI_KEY
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = "What is the capital of Paris?"

#==> Old OpenAI version code : 
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[{"role": "user", "content": prompt}],
#     max_tokens=200
# )
# print(response.choices[0].message.content.strip())

#==> New OpenAI version code : 
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI()

response = client.responses.create(
    # model="gpt-4o-mini",
    model="gpt-5.6-luna",
    # model="gpt-6-astra",
    # input="Write a one-sentence bedtime story about a unicorn.",
    input=prompt,
)

print(response.output_text) 


"""
[
  {
    "id": "msg_67b73f697ba4819183a15cc17d011509",
    "type": "message",
    "role": "assistant",
    "content": [
      {
        "type": "output_text",
        "text": "Under the soft glow of the moon, Luna the unicorn danced through fields of twinkling stardust, leaving trails of dreams for every child asleep.",
        "annotations": []
      }
    ]
  }
]
"""



