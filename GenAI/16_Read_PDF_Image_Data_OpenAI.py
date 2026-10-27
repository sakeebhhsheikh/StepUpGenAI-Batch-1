# import requests

# url = 'https://rubiconrecycling.co/wp-content/uploads/2026/08/rome-price-sheet-8-3-26.pdf'


# resp  = requests.get(url)

# print(resp.status_code)

# with open('rubicon.pdf', 'wb') as fobj:
#     fobj.write(resp.content)
#-----------------------------------------------------
import os
import json
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

# Load API key from .env
load_dotenv()

client = OpenAI()

file = client.files.create(
    file=open('rubicon.pdf', 'rb'),
    purpose="user_data",
)

Prompt = """
Extract ONLY the data data from the PDF.

We need only these three COLUMNS:

Commodity
CODE
Base

IMPORTANT RULES : 

1. EXTRACT each row from the table.
2. Preserve the text exactly as it appears.
3. Preserve all digits exactly as they appear.
4. Preserve decimal values exactly.
5. Do not infer or calculate values.
6. Do not correct spelling or Capitalization.
7. Ignore commpletely blank rows.
8. Do not include Column Headers.
9. Never guess a missing value.


Return : 

{
    "Commodity" : "Al/Cu Rads",
    "Code":"3670",
    "Base":"2.77"
}

Use null for blank fields.

"""


response = client.responses.create(
    model = "gpt-6-luna",
    reasoning = {"effort" : "low"},
    input = [
        {
            "role" : "user",
            "content" : [
                {
                    "type":"input_file",
                    "file_id":file.id,
                },
                {
                    "type":"input_text",
                    "text":Prompt,
                }
            ]
        }
    ]
)


data = json.loads(response.output_text)


for row in data:
    for field in ["Commodity","Code","Base"]:
        if field not in row:
            row[field] = None


df = pd.DataFrame(data, columns=["Commodity","Code","Base"])
print(df.head())
df.to_csv('Rubicol_csv_data.csv', index=False)