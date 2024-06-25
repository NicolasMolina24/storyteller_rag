
def generate(state):
    """Generate a response
    
    Args:
        state(dict): The current graph state
            Uses the following keys:
                question: question or query to be answered
                documents: list of documents
                runnable['rag_chain']: Runnable to be executed
        
    Returns:
        The response
    """
    print("---GENERATE---")
    question = state["question"]
    documents = state["documents"]
    rag_chain = state["runnable"]["rag_chain"]
    if not isinstance(documents, list):
        documents = [documents]
    # RAG generation
    generation = rag_chain.invoke({"context": documents, "question": question})
    return {"generation": generation}