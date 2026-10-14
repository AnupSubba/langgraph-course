from langchain_tavily import TavilySearch
from openai.types.beta.beta_namespace_tool import Tool
from dotenv import load_dotenv

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

load_dotenv()

@tool
def triple(num:float) -> float:
    """
    param num: a number to triple
    return: a number that is tripled
    """
    return float(num) * 3

tools = [TavilySearch(max_results=1), triple]
llm = ChatOpenAI(model="gpt-5.1", temperature=0).bind_tools(tools)