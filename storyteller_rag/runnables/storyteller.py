# Importing the necessary libraries
from langchain_core.prompts import ChatPromptTemplate
from langchain.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from storyteller_rag.prompts import PROMPTS

# Router model: gpt-3.5-turbo | temperature: 0 | prompt
# 1. Define the model for the agent
class StoryQuote(BaseModel):
    """Create a story from a quote"""
    story: str = Field(
        description="Story created from the quote"
    )
    quote: str = Field(
        description="Quote to create a story"
    )
    author: str = Field(
        description="Author of the quote"
    )
    category: str = Field(
        description="Category of the quote"
    )


def runnables_storyteller():
    """Create a story from a quote
    
    Returns:
        Runnable to create a story from a quote"""
    # 2. Create the chat
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )
    # 3. Bound the tool and structure the output
    structured_llm_story = llm.with_structured_output(StoryQuote)
    # 4. Create the prompt
    system_prompt = PROMPTS['storyteller']
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "quote: {quote} \n\n author: {author} \n\n category: {category}")
        ]
    )
    # 5. Create the LCE
    return prompt | structured_llm_story