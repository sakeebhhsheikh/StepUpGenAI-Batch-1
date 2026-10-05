from openai import OpenAI
import os
from dotenv import load_dotenv
import json

# OPENAI_API_KEY --> Standard name for OPENAI api key
# Load API key from .env
load_dotenv()

def get_weather(city):
    # Pretend this came from a weather API
    return {
        "city": city,
        "temperature": 32,
        "condition": "Sunny"
    }

def calculate_tax(income, rate):
    if income>1200000:
        calculated_tax = ((income-1200000)*0.3)
    else:
        calculated_tax = 0
    return {"calculated_tax":calculated_tax}


tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Get weather information for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string"
                }
            },
            "required": ["city"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "calculate_tax",
        "description": "Calculate tax.",
        "parameters": {
            "type": "object",
            "properties": {
                "income": {"type": "number"},
                "rate": {"type": "number"}
            },
            "required": ["income", "rate"],
            "additionalProperties": False
        }
    }
]


client = OpenAI()

# input_list = [{"role": "user", "content":"What's the weather in Mumbai?"},]
input_list = [{"role": "user", "content":"My salary income is 1400000. what will be my tax this year with tax slab rate 30% ?"},]
response = client.responses.create(
    model="gpt-5.6-luna",
    input=input_list,
    tools=tools
)

if response.output[0].type == "function_call":
    print('Choosen Function call : ', response.output[0].name)

print(response)
print("===================================")

# for item in response.output:

#     if item.type == "function_call":

#         name = item.name
#         arguments = json.loads(item.arguments)

#         if name == "get_weather":
#             result = get_weather(arguments["city"])

#             print(result)



# Response(id='resp_0d13587e3b6f7777006abc8fd33f7887d196602f403776a160', created_at=1790742483.0, error=None, incomplete_details=None, instructions=None, metadata={}, model='gpt-5.6-luna', object='response', output=[ResponseFunctionToolCall(arguments='{"city":"Mumbai"}', call_id='call_5laaqPvLvE0AcHNoVUDAUoNO', name='get_weather', type='function_call', id='fc_0d13587e3b6f7777006abc8fd3f84887d1abb1e441c335e303', async_=None, caller=None, namespace=None, status='completed')], parallel_tool_calls=True, temperature=1.0, tool_choice='auto', tools=[FunctionTool(name='get_weather', parameters={'type': 'object', 'properties': {'city': {'type': 'string'}}, 'required': ['city'], 'additionalProperties': False}, strict=True, type='function', allowed_callers=None, async_=None, defer_loading=None, description='Get weather information for a city.', output_schema=None)], top_p=0.98, background=False, completed_at=1790742484.0, conversation=None, max_output_tokens=None, max_tool_calls=None, moderation=None, previous_response_id=None, prompt=None, prompt_cache_diagnostics=None, prompt_cache_key=None, prompt_cache_options=None, prompt_cache_retention='24h', reasoning=Reasoning(context='all_turns', effort='medium', generate_summary=None, mode='standard', summary=None), safety_identifier=None, service_tier='default', status='completed', text=ResponseTextConfig(format=ResponseFormatText(type='text'), verbosity='medium'), top_logprobs=0, truncation='disabled', usage=ResponseUsage(input_tokens=49, input_tokens_details=InputTokensDetails(cache_write_tokens=0, cached_tokens=0), output_tokens=18, output_tokens_details=OutputTokensDetails(reasoning_tokens=0), total_tokens=67), user=None, access_programs=None, billing={'payer': 'developer'}, frequency_penalty=0.0, presence_penalty=0.0, store=True, tool_usage={'image_gen': {'input_tokens': 0, 'input_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'output_tokens': 0, 'output_tokens_details': {'image_tokens': 0, 'text_tokens': 0}, 'total_tokens': 0}, 'web_search': {'num_requests': 0}})


# output=[ResponseFunctionToolCall(
#     arguments='{"city":"Mumbai"}', 
#     call_id='call_5laaqPvLvE0AcHNoVUDAUoNO', 
#     name='get_weather', 
#     type='function_call', 
#     id='fc_0d13587e3b6f7777006abc8fd3f84887d1abb1e441c335e303', 
#     async_=None, caller=None, namespace=None, status='completed')]



# Save function call outputs for subsequent requests
"""
input_list += response.output

for item in response.output:
    if item.type == "function_call":
        if item.name == "get_weather":
            # 3. Execute the function logic for get_horoscope
            city = json.loads(item.arguments)["city"]
            result = get_weather(city)

            # 4. Provide function call results to the model
            input_list.append(
                {
                    "type": "function_call_output",
                    "call_id": item.call_id,
                    "output": json.dumps(result),
                }
            )

# print("Final input:")
# print(input_list)

response = client.responses.create(
    model="gpt-5.6-luna",
    tools=tools,
    input=input_list,
)

# 5. The model should be able to give a response!
print("Final output:")
print(response.model_dump_json(indent=2))
print("\n" + response.output_text)"""


#===========================================================================
