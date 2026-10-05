from openai import OpenAI
import os
from dotenv import load_dotenv

# OPENAI_API_KEY --> Standard name for OPENAI api key
# Load API key from .env
load_dotenv()

client = OpenAI()

# def ask_ai(prompt, previous_resp_id, model="gpt-4o-mini"):

#     instructions = """
#         You are a python trainer for Generative AI
    
#         Rules:
#         1. Give short answers for questions.
#         2. Give small example.
#         """

#     kwargs = {"model" : model,
#               "instructions" :instructions,
#               "input" : prompt,
#               "max_output_tokens" : 100,
#               }
#     if previous_resp_id:
#         kwargs["previous_response_id"] = previous_resp_id

    
#     response = client.responses.create(
#         **kwargs
#     )
#     return response

# previous_resp_id = None
# while True:
#     inp = input('Enter your query : ')
#     if 'exit' in inp.lower().split() or 'stop' in inp.lower().split():
#         print('Thank you talking to me...')
#         break

#     response = ask_ai(inp, previous_resp_id)
#     previous_resp_id = response.id
#     model_answer = response.output_text
#     print(model_answer)


# ###########################################################################

# response2 = client.responses.create(
#     model="gpt-4o-mini",
#     previous_response_id=response1.id,
#     input="What is my name?"
# )
# print(response2.output_text)

# ###########################################################################

# from openai import OpenAI

# client = OpenAI()

# previous_response_id = None

# while True:
#     user_input = input("You: ")

#     if user_input.lower() in ["exit", "quit"]:
#         break

#     kwargs = {
#         "model": "gpt-4o-mini",
#         "input": user_input
#     }
#     if previous_response_id:
#         kwargs["previous_response_id"] = previous_response_id


# ###########################################################################

# response = client.responses.create(
#     model="gpt-4o-mini",
#     input="Write a long explanation of Python."
# )

# print(response.output_text)

# ###########################################################################

# stream = client.responses.create(
#     model="gpt-4o-mini",
#     input="Write a long explanation of Python.",
#     max_output_tokens=100,
#     stream=True
# )

# for event in stream:
#     print(event)



# {
#     "name": "John",
#     "age": 30,
#     "city": "Mumbai"
# }


# from openai import OpenAI

# client = OpenAI()

# response = client.responses.create(
#     model="gpt-5.6-luna",
#     input="Extract: John is 30 years old and lives in Mumbai.",
#     text={
#         "format": {
#             "type": "json_schema",
#             "name": "person",
#             "strict": True,
#             "schema": {
#                 "type": "object",
#                 "properties": {
#                     "name": {
#                         "type": "string"
#                     },
#                     "age": {
#                         "type": "integer"
#                     },
#                     "city": {
#                         "type": "string"
#                     }
#                 },
#                 "required": [
#                     "name",
#                     "age",
#                     "city"
#                 ],
#                 "additionalProperties": False
#             }
#         }
#     }
# )

# print(response.output_text)


# #####################################################################################
# import json

# data = json.loads(response.output_text)

# print(data["name"])
# print(data["age"])
# print(data["city"])


# from dataclasses import dataclass
# @dataclass
# class MyClass:
#     eno : int
#     ename : str
#     esal : float


# class MyClass:
#     def __int__(self, eno:int, ename:str, esal:float):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal






#####################################################################################

# pip install pydantic

from pydantic import BaseModel
from openai import OpenAI

client = OpenAI()


class Person(BaseModel):
    name: str
    age: int
    city: str


response = client.responses.parse(
    model="gpt-5.6-luna",
    input="John is 30 years old and lives in Mumbai.",
    text_format=Person,
)

person = response.output_parsed

print("Name:", person.name)
print("Age:", person.age)
print("City:", person.city)
#####################################################################################