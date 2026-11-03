# pip install -U langchain langchain-core langchain-ollama
"""
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()


#Initialize the LLM model
llm = ChatOllama(
    model = "llama3.2:3b",
    temperature=0.3
)


messages = [
    SystemMessage(
        content="Your are a langchain pipeline expert"
    ),
    HumanMessage(
        content="Provide step by step approach to implement RAG application pipeline with structured output using pydantic."
    )
]

#Query LLM Model
response = llm.invoke(
    messages
)


#printing LLM reponse
print("Response ::", "\n", response.content)
print("MetaData ::", "\n", response.usage_metadata)
"""


#========================================================================================================================

"""
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


#Initialize the LLM model
llm = ChatOllama(
    model = "llama3.2:3b",
    temperature=0.3
)

# name = "sakeeb"
# print(f"hello, {name}")

prompt = ChatPromptTemplate.from_template(
    "You are a python expert, Please explain {topic} in less than 50 words"
)

parser = StrOutputParser()


chain = prompt | llm | parser


#Query LLM Model
response = chain.invoke({
    "topic":"python Decorators"
})


#printing LLM reponse
print(response)"""

#========================================================================================================================

#==> HuggingFace - Run Local models through transformers pipeline

# "meta-llama/Llama-3.1-8B-Instruct"

# "meta-llama/Llama-3.2-3B-Instruct"


# ['any-to-any', 'audio-classification', 'automatic-speech-recognition', 'depth-estimation', 'document-question-answering', 
#  'feature-extraction', 'fill-mask', 'image-classification', 'image-feature-extraction', 'image-segmentation', 'image-text-to-text',
#   'keypoint-matching', 'mask-generation', 'ner', 'object-detection', 'sentiment-analysis', 'table-question-answering', 
#   'text-classification', 'text-generation', 'text-to-audio', 'text-to-speech', 'token-classification', 'video-classification', 
#  'zero-shot-audio-classification', 'zero-shot-classification', 'zero-shot-image-classification', 'zero-shot-object-detection']

#==> Using Pipeline Directly :

from transformers import pipeline

generator = pipeline(
    task="text-generation",
    model="HuggingFaceTB/SmolLM2-360M-Instruct"
)

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "Write a poem on Hugging Face, the company"
    },
]


result = generator(
    messages,
    max_new_tokens=100,
)


# print(result)
print(result[0]['generated_text'][-1]['content'])

# [{
#     'generated_text': [
#         {'role': 'system', 'content': 'You are a helpful assistant.'}, 
#         {'role': 'user', 'content': 'Write a poem on Hugging Face, the company'}, 
#         {'role': 'assistant', 'content': 'Hugging Face, the company\n\nAt the heart of the digital world\n\nA symbol of kindness, a beacon\n\nA face that brings light, comfort, and trust\n\nIn the digital, physical realm\n\nA friend, a companion, a friend\n\nA reminder of human connection\n\nA symbol of empathy and understanding\n\nA beacon of positivity and hope\n\nA reminder of the importance of kindness and compassion\n\nA symbol of trust in a world of digital chaos'}
#                       ]
# }
#  ]

"""
Hugging face, a beacon of warmth,
A symbol of kindness, a light to guide,
Your face shines bright, a testament to cheer,
Your smile, a ray of joy, a reminder to cheer.

Your face is a canvas of beauty, a masterpiece to behold,
With every smile, a promise of love to hold,
Your face can be a friend, a confidant, a friend to be,
A reminder of the kind words, to be
"""
#================================================================================================================
"""
from dotenv import load_dotenv
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


hf_pipe = pipeline(
    task="text-generation",
    model="HuggingFaceTB/SmolLM2-360M-Instruct",
    max_new_tokens=100,
    do_sample=False,
    return_full_text=False
)

#Initialize the LLM model
llm = HuggingFacePipeline(pipeline=hf_pipe)



prompt = PromptTemplate.from_template(
    "You are a python expert, Please explain {topic} in less than 50 words"
)

parser = StrOutputParser()


chain = prompt | llm | parser


#Query LLM Model
response = chain.invoke({
    "topic":"python Decorators"
})


#printing LLM reponse
print(response)
"""


"""
Python Decorators are a powerful feature in Python that allows you to modify the behavior of a function without changing its source code. They are used to add new functionality to existing functions, such as logging, authentication, caching, and more.

A decorator is a small function that takes another function as an argument and returns a new function that "wraps" the original function. It can modify the behavior of the original function by adding or removing functionality, and it can also be
"""