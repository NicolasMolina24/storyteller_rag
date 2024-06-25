
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from storyteller_rag.prompts import PROMPTS

def runnable_memory():
    """
    This function defines the memory runnable
    
    Returns:
        The memory chain"""
    # Define the system prompt
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", PROMPTS["memory_history"]),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ]  
    )

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )

    return prompt | llm