# pip install anthropic
import anthropic
from dotenv import load_dotenv

#Note : Copy you API_KEY to .env file with name : ANTHROPIC_API_KEY="your_api_key"

# Load API key from .env
load_dotenv()

client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "Hello, Claude",
        }
    ],
)
for block in message.content:
    if block.type == "text":
        print(block.text)


#==> Important Learning and platform links : 
# https://claude.ai/    ==> Messaging tool
# https://platform.claude.com/  ==> API and Documentation
# https://anthropic.skilljar.com/ ==> Free Learning courses
# https://anthropic-partners.skilljar.com/  ==> Paid Learning cources
# https://platform.claude.com/docs/en/api/overview  ==> API Reference
# https://platform.claude.com/docs/en/api/python/messages ==> Messages API
