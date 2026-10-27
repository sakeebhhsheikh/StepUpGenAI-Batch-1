# MODEL LINK : https://docs.langchain.com/oss/python/langchain/models#basic-usage
# MESSAGES : https://docs.langchain.com/oss/python/langchain/messages


# pip install -qU langchain "langchain[huggingface]"
import os
from langchain.agents import create_agent
from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="openai:gpt-5.5",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
print(result["messages"][-1].content_blocks)



#--------------------------------------------------------------------------------------------------
from pydantic import BaseModel, Field
import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

# os.environ["OPENAI_API_KEY"] = "sk-..."

model = init_chat_model("gpt-5.5")

class Movie(BaseModel):
    """A movie with details."""
    title: str = Field(description="The title of the movie")
    year: int = Field(description="The year the movie was released")
    director: str = Field(description="The director of the movie")
    rating: float = Field(description="The movie's rating out of 10")

model_with_structure = model.with_structured_output(Movie)
response = model_with_structure.invoke("Provide details about the movie Inception")
print(response)  # Movie(title="Inception", year=2010, director="Christopher Nolan", rating=8.8)

#------------------------------------------------------------------------------------------------------
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()


model = init_chat_model("gpt-5.5")

response = model.invoke("Why do parrots have colorful feathers?")
print(response)

conversation = [
    {"role": "system", "content": "You are a helpful assistant that translates English to French."},
    {"role": "user", "content": "Translate: I love programming."},
    {"role": "assistant", "content": "J'adore la programmation."},
    {"role": "user", "content": "Translate: I love building applications."}
]

response = model.invoke(conversation)
print(response)  # AIMessage("J'adore créer des applications.")

#------------------------------------------------------------------------------------------------------

#==> Streaming data

for chunk in model.stream("Why do parrots have colorful feathers?"):
    print(chunk.text, end="|", flush=True)

#------------------------------------------------------------------------------------------------------

from pydantic import BaseModel, Field, Optional

class UniversityRecords(BaseModel):
    university : str = Field(description="University Name")
    address : str = Field(description="University Address")
    vc : Optional[str] = Field(description="University Vice Chancellor")
    registrar : Optional[str] = Field(description="University Registrar")
    vc_email : Optional[str] = Field(description="University VC email")
    reegistrar_email : Optional[str] = Field(description="University Registrar email")


text_format = UniversityRecords


university = response.outparsed

#-> To_dict
record = university.model_dump()

#-> To_JSON
record = university.model_dump_json(indent=2)

#--------------------------------------------------------------------------------------------

"""
Parameters
A chat model takes parameters that can be used to configure its behavior. The full set of supported parameters varies by model and provider, but standard ones include:
​
model
string
required
The name or identifier of the specific model you want to use with a provider. You can also specify both the model and its provider in a single argument using the ’:’ format, for example, ‘openai:o1’.
​
api_key
string
The key required for authenticating with the model’s provider. This is usually issued when you sign up for access to the model. Often accessed by setting an environment variable.
​
temperature
number
Controls the randomness of the model’s output. A higher number makes responses more creative; lower ones make them more deterministic.
​
max_tokens
number
Limits the total number of tokens in the response, effectively controlling how long the output can be.
​
timeout
number
The maximum time (in seconds) to wait for a response from the model before canceling the request.
​
max_retries
number
default:"6"
The maximum number of attempts the system will make to resend a request if it fails due to issues like network timeouts or rate limits. Retries use exponential backoff with jitter. Network errors, rate limits (429), and server errors (5xx) are retried automatically. Client errors such as 401 (unauthorized) or 404 are not retried. For long-running agent tasks on unreliable networks, consider increasing this to 10–15.
"""

model = init_chat_model(
    "claude-sonnet-4-6",
    # Kwargs passed to the model:
    temperature=0.7,
    timeout=30,
    max_tokens=1000,
    max_retries=6,  # Default; increase for unreliable networks
)