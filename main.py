
from langgraph.graph import END, StateGraph
from typing import List, Dict
from typing_extensions import TypedDict
import operator
from langchain_core.messages import BaseMessage
from langchain_core.runnables.base import Runnable

from storyteller_rag.edges import edges
from storyteller_rag.nodes import (
    grade_node, memory_node, generate_node,
    quote_node, save_memory_node, web_node,
    storyteller_node, retrieve_node
    )
from storyteller_rag.runnables.route_question import runnables_route_question
from storyteller_rag.runnables.web import runnable_web_search
from storyteller_rag.runnables.memory_chain import runnable_memory
from storyteller_rag.runnables.grade import runnables_grade_question
from storyteller_rag.runnables.generate import runnables_generate
from storyteller_rag.runnables.storyteller import runnables_storyteller
from storyteller_rag.runnables.retriever_vector_storage import vector_storage_as_retreiver
from storyteller_rag.runnables.quote import runnable_quote
from storyteller_rag.utils import create_vectorstorage
from storyteller_rag.utils import get_by_session_id

import dotenv
dotenv.load_dotenv()

# Create the data for the state
def create_state_data():
    """
    Create the data for the state
    
    Returns:
        Dict: data for the state"""

    # Docs to index
    urls = [
        "https://en.wikipedia.org/wiki/Artificial_intelligence",
        "https://en.wikipedia.org/wiki/Machine_learning"
    ]
    # create vector storage
    vector_storage = create_vectorstorage(urls)
    session = 'user_1'
    storage = {}
    storage = get_by_session_id(storage, session)
    # create the data and placeholder 
    data = {
        'runnable': {
            'query_router': runnables_route_question(),
            'get_quote': runnable_quote(),
            'web_search': runnable_web_search(),
            'memory_chain': runnable_memory(),
            'grade_documents': runnables_grade_question(),
            'rag_chain': runnables_generate(), # generate
            'storyteller': runnables_storyteller(),
            'vector_storage_retriever': vector_storage_as_retreiver(vector_storage=vector_storage)
        },
        'question': '',
        'generation': '',
        'documents': [],
        'memory': storage
    }
    return data

def create_app():
    """
    Create the app
    """
    # Defining the nodes funtions
    # edge funtion
    route_question = edges.route_question
    # nodes funtions
    get_quote = quote_node.get_quote
    web_search = web_node.web_search
    memory_history = memory_node.memory_history
    grade = grade_node.grade
    generate = generate_node.generate
    save_memory = save_memory_node.save_memory
    storyteller = storyteller_node.storyteller
    retriver = retrieve_node.retrieve


    class GraphState(TypedDict):
        """
        Reprsents the state of the graph

        Attributes:
            question: question or query to be answered
            generation: LLM generation
            documents: list of documents
            memory: list of messages in the session
        """
        runnable: Dict[str, Runnable]
        question: str
        generation: str
        documents: List[str]
        memory: list[BaseMessage, operator.add]


    workflow = StateGraph(GraphState)


    # defining the entry point
    workflow.set_conditional_entry_point(
        route_question,
        {
            "retrieve": "retrieve",
            "web_search": "web_search",
            "get_quote": "get_quote",
            "memory_history": "memory_history",
        }
    )

    # Nodes
    workflow.add_node("retrieve", retriver)
    workflow.add_node("web_search", web_search)
    workflow.add_node("get_quote", get_quote)
    workflow.add_node("memory_history", memory_history)
    workflow.add_node("grade", grade)
    workflow.add_node("generate", generate)
    workflow.add_node("save_memory", save_memory)
    workflow.add_node("storyteller", storyteller)

    # Edges
    workflow.add_edge("retrieve", "grade")
    workflow.add_edge("web_search", "grade")
    workflow.add_edge("get_quote", "storyteller")
    workflow.add_edge("storyteller", "save_memory")
    workflow.add_edge("grade", "generate")
    workflow.add_edge("generate", "save_memory")
    workflow.add_edge("memory_history", "save_memory")
    workflow.add_edge("save_memory", END)

    # Compile
    return workflow.compile()
