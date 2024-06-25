from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from storyteller_rag.prompts import PROMPTS


def runnables_generate():
    """Generate a response

    Returns:
        Runnable to generate a response
    """
    # prompt
    prompt = PROMPTS['generate']

    # Define LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )
    # Create the chain
    return prompt | llm | StrOutputParser()