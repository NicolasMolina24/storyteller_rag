# Importing the necessary libraries
from typing import Dict, List
import requests
import os
from langchain.pydantic_v1 import BaseModel, Field
from langchain_core.tools import StructuredTool
from langchain_core.tools import ToolException
from langchain_core.messages import AIMessage
from langchain_openai import ChatOpenAI

APININJA_KEY = os.getenv("APININJA_KEY")

# Defining the tool
class CategoryQuote(BaseModel):
    """Category to request a quote for"""
    category: str = Field(description="Category to request a quote for")


# Core function for request a quote
def get_a_quote(category: str) -> str:
    """Request for a quote"""
    api_url = f'https://api.api-ninjas.com/v1/quotes?category={category}'
    # Specify a timeout (e.g., 10 seconds)
    response = requests.get(api_url, headers={'X-Api-Key': APININJA_KEY}, timeout=10)
    if response.status_code == requests.codes.ok:
        return response.text
    else:
        raise ToolException(f"""Error calling to API, {
                            response.status_code}, {response.text}""")

def runnable_quote():
    """Runnable for quote generation.
    This runnable uses the API-Ninjas API to get a quote.
    
    Returns:
        The agent chain"""
    # Create the tool
    quote_tool = StructuredTool.from_function(
        func=get_a_quote,
        name="Quote",
        handle_tool_error=True,
        args_schema=CategoryQuote,
    )
    tools = [quote_tool]
    # _________________________________________________________
    # Definig the llm
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
    # bind the tool to a llm
    llm_quote = llm.bind_tools([quote_tool])


    # Create a function to call the tools and select the one choosed by the llm
    def call_tools(msg: AIMessage) -> List[Dict]:
        """Simple sequential tool calling helper."""
        tool_map = {tool.name: tool for tool in tools}
        tool_calls = msg.tool_calls.copy()
        for tool_call in tool_calls:
            tool_call["output"] = tool_map[tool_call["name"]].invoke(
                tool_call["args"])
        return tool_calls
    # Create the agent chain
    return llm_quote | call_tools
