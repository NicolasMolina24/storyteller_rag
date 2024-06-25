from typing import Dict
from langchain_core.chat_history import BaseChatMessageHistory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain.memory import ChatMessageHistory
from langchain_openai import OpenAIEmbeddings

import os

def set_memory(chat_history: BaseChatMessageHistory, ai_message=None, user_message=None):
    """
    Save the chat history to the memory store.
    
    Args:
        chat_history: The chat history to save

    Returns:
        BaseChatMessageHistory: The chat history
    """
    if ai_message:
        chat_history.add_ai_message(ai_message)
    if user_message:
        chat_history.add_user_message(user_message)
    return chat_history


def create_vectorstorage(urls: list[str]):

    # Load the embeddings
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))

    # Load documents
    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]

    # Split documents
    # Define the splitter
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=512,
        chunk_overlap=16
    )
    # split the documents
    doc_splitted = text_splitter.split_documents(docs_list)


    # create simple ids
    ids = [str(i) for i in range(1, len(doc_splitted) + 1)]

    # Add the documents to the vector store
    vector_storage = Chroma.from_documents(
        # collection_name="wiki_articles",
        documents=doc_splitted,
        embedding=embeddings,
        ids=ids
    )
    return vector_storage


def get_by_session_id(memory_store: Dict, session_id: str) -> BaseChatMessageHistory:
    if session_id not in memory_store:
        memory_store[session_id] = ChatMessageHistory()
    return memory_store[session_id]



