def retrieve(state):
    """
    Retreive documents
    
    Args:
        state(dict): The current graph state
            Uses the following keys:
                runnable['vector_storage_retriever']: Runnable to be executed
                question: The question or query to be answered
    Returns:
        The documents"""
    print("------- RETRIEVING DOCUMENTS -------")
    question = state["question"]
    vector_storage_retriever = state["runnable"]["vector_storage_retriever"]

    # Retrieve documents
    docs = vector_storage_retriever.invoke(question)
    return {"documents": docs, "question": question}