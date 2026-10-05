# 1. Direct file input --> There is only file to query
# 2. Creating Vector store -> There are multiple file to query from.


# OPENAI_KEY
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API key from .env
load_dotenv()

client = OpenAI()

# with open() as fobj:
#     fileobj = open("", "rb")

#     file = client.files.create(
#         file=fileobj,
#         purpose="user_data"
#     )
file = client.files.create(file=open(r"C:\Users\HP.DESKTOP-SSLBTGT\Desktop\PythonGenAI\StepUpGenAI-Batch-1\GenAI\file_image_Input_pdf.pdf", "rb"), purpose="user_data")

# print(file.id)
# print(file)

# file-YCY5jrLRaFh5yMCTn5nBmq
# FileObject(id='file-YCY5jrLRaFh5yMCTn5nBmq', 
#            bytes=850071, 
#            created_at=1790914920, 
#            filename='file_image_Input_pdf.pdf', 
#            object='file', 
#            purpose='user_data', 
#            status='processed', 
#            expires_at=None, 
#            status_details=None)

#------------------------------------------------------------
query = """from the given pdf extract Commodity, CODE, Base
It may contain image so process image and extract data.
if it contain an image improve the DPI level for image to extract correct values
Give me structured output
"""

# response = client.responses.create(
#     model="gpt-4.1",
#     input=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_file",
#                     "file_id": file.id,
#                 },
#                 {
#                     "type": "input_text",
#                     "text": query,
#                 },
#             ],
#         }
#     ],
# )

# print(response.output_text)

#==================================================================================
#-> Storing file in a vector store : 

vector_store = client.vector_stores.create(        # Create vector store
    name="Novel",
)

client.vector_stores.files.upload_and_poll(        # Upload file
    vector_store_id=vector_store.id,
    file=open(r"C:\Users\HP.DESKTOP-SSLBTGT\Desktop\PythonGenAI\StepUpGenAI-Batch-1\GenAI\To sir with love - Novel.pdf", "rb")
)

print(vector_store.id)

"""
vector_store_id = vector_store.id

query = "who is the narrator and what is this novel about?"
response = client.responses.create(
    model="gpt-5.6-luna",
    input=query,
    tools=[{"type": "file_search", "vector_store_ids": [vector_store_id]}],
)
print(response.output_text)
"""

# response = client.responses.create(
#     model="gpt-5.6-luna",
#     input=query,
#     tools=[
#         {
#             "type": "file_search",
#             "vector_store_ids": [vector_store_id],
#             "max_num_results": 2,
#         }
#     ],
# )
# print(response)
#================================================================
#==> Using Vectore store tool to search a file
user_query = "who is the narrator and what is this novel about?"

results = client.vector_stores.search(
    vector_store_id=vector_store.id,
    query=user_query,
)

print(results.data)