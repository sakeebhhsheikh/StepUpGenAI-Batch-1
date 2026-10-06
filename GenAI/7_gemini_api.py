# pip install google-generativeai==0.8.6
# pip install google-genai
# https://pypi.org/project/google-genai/

import os

# GEMINI_API_KEY="YOUR_API_KEY"   ==> Default api key var name in .env

# must be set BEFORE importing google.generativeai
os.environ["GRPC_VERBOSITY"] = "NONE"
os.environ["GLOG_minloglevel"] = "3"  # 3 = FATAL only

#####################################################
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel("gemini-3.8-flash")

# response = model.generate_content("Explain python-lists in short and simple")
# print(response.text)

########################################################

from google import genai
from dotenv import load_dotenv

load_dotenv()

###############################################################
client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain python-lists in short and simple"
)
print(interaction.output_text)

###############################################################

# Stream the response
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3.8-flash",
    input="Explain how AI works",
    stream=True
)
for event in stream:
    print(event)

###############################################################

# Multi-turn conversations 

from google import genai

client = genai.Client()

# Server-side state (recommended)
interaction1 = client.interactions.create(
    model="gemini-3.8-flash",
    input="I have 2 dogs in my house.",
)
print("Response 1:", interaction1.output_text)

interaction2 = client.interactions.create(
    model="gemini-3.8-flash",
    input="How many paws are in my house?",
    previous_interaction_id=interaction1.id,
)
print("Response 2:", interaction2.output_text)

###############################################################

#File Input : 

#--> Direct Input:
#--> File encoding
#--> Types of files : image, txt, doc, pdf, mp3, wav, mp4

# import base64
# from google import genai

# client = genai.Client()

# # Load a local image
# with open("sample.jpg", "rb") as f:
#     image_bytes = f.read()
# image_b64 = base64.b64encode(image_bytes).decode("utf-8")

# interaction = client.interactions.create(
#     model="gemini-3.8-flash",
#     input=[
#         {
#             "type": "text", 
#             "text": "Compare this local image and this remote audio file."
#         },
#         {
#             "type": "image",
#             "data": image_b64,
#             "mime_type": "image/jpeg"
#         },
#     ]
# )
# print(interaction.output_text)
#=====================================================================
# from google import genai

# client = genai.Client()

# interaction = client.interactions.create(
#     model="gemini-3.8-flash",
#     input=[
#         {
#             "type": "text", 
#             "text": "Compare this local image and this remote audio file."
#         },
#         {
#             "type": "image",
#             "uri": "https://storage.googleapis.com/generativeai-downloads/data/sample.jpg",
#             "mime_type": "image/jpeg"
#         },
#     ]
# )
# print(interaction.output_text)

#=====================================================================

# generation ==>

# import base64
# from google import genai

# client = genai.Client()

# interaction = client.interactions.create(
#     model="gemini-3.1-flash-image",
#     input="Generate an image of a futuristic city skyline at sunset",
# )

# with open("generated_image.png", "wb") as f:
#     f.write(base64.b64decode(interaction.output_image.data))


#=====================================================================
#S==> tructured output : 

# from google import genai
# from pydantic import BaseModel, Field
# from typing import List, Optional

# class Recipe(BaseModel):
#     recipe_name: str = Field(description="Name of the recipe.")
#     ingredients: List[str] = Field(description="List of ingredients.")
#     prep_time_minutes: Optional[int] = Field(description="Prep time in minutes.")

# client = genai.Client()

# interaction = client.interactions.create(
#     model="gemini-3.8-flash",
#     input="Give me a recipe for banana bread",
#     response_format={
#         "type": "text",
#         "mime_type": "application/json",
#         "schema": Recipe.model_json_schema()
#     },
# )

# recipe = Recipe.model_validate_json(interaction.output_text)
# print(recipe)


#Ref : https://aistudio.google.com/docs/get-started
#Creating API KEY : https://aistudio.google.com/api-keys


# Text generation: System instructions, generation config, and advanced text patterns.
# Image generation: Aspect ratios, image editing, and style references.
# Image understanding: Classification, object detection, and visual Q&A.
# Thinking: Use chain-of-thought reasoning for complex tasks.
# Function calling: Parallel, compositional, and constrained function modes.
# Google Search: Grounding, citations, and search suggestions.
# Structured output: JSON schemas, enums, and recursive type definitions.
# Managed Agents: Pre-built agents with code execution and file management.
# Deep Research: Autonomous multi-step research with planning and synthesis.

#=> Claude

#=> HuggingFace
#=> Olama

#=> Framworks : LangChain, Langgraph, Neo4j, 
#=> Tracking : LangFuse

#==> Fine-Tuning