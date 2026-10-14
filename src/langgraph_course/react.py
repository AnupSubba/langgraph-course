from dotenv import load_dotenv
import os

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()


def triple(num: float) -> float:
    return num * 3

if __name__ == "__main__":
    llm = ChatOpenAI(model="gpt-5.1")
    print(llm.invoke("Hello, how are you?"))