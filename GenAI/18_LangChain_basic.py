"""from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()


#Initialize the LLM model
llm = ChatOpenAI(
    model = "gpt-4.1-mini",
    temperature=0.3
)

#Query LLM Model
response = llm.invoke(
    "list important tool provided by langchain"
)


#printing LLM reponse
print(response.content)
"""

#=================================================================================
"""from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()


#Initialize the LLM model
llm = ChatOpenAI(
    model = "gpt-4.1-mini",
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
print(response.content)"""

#=======================================================================================================
"""
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()


#Initialize the LLM model
llm = ChatOpenAI(
    model = "gpt-4.1-mini",
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
print(response.content)
"""

#=======================================================================================================
"""
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


#Initialize the LLM model
llm = ChatOpenAI(
    model = "gpt-4.1-mini",
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
print(response)
"""

