
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from storyteller_rag.prompts import PROMPTS
from langchain.pydantic_v1 import BaseModel, Field

# Router model: gpt-3.5-turbo | temperature: 0 | prompt
# 1. Define the model for the agent
class GradeDocumnets(BaseModel):
    """Binary score for relevance of documents"""
    binary_core: str = Field(
        description="Grade if the document is relevant or not with 'yes'/ 'no'"
    )

def runnables_grade_question():
    """Grade the relevance of documents to a user question
    
    Returns:
        Runnable to grade the relevance of documents to a user question"""
    # 2. Create the chat
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0
    )
    # 3. Bound the tool and structure the output
    structured_llm_grader = llm.with_structured_output(GradeDocumnets)
    # 4. Create the prompt
    system_prompt = PROMPTS["grade"]
    grade_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "Retrieve document: \n\n {document}\n\n question is: {question}")
        ]
    )
    # 5. Create the LCE
    return grade_prompt | structured_llm_grader