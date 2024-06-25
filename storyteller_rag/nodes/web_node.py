
def web_search(state):
    """Given a question, search the web for an answer

    Args:
    Args:
        state(dict): The current graph state
            Uses the following keys:
                runnable['web_search']: Runnable to be executed
                question: The question or query to be answered
    
    Returns:
        List of the documents from the web search
    """
    print("------- WEB SEARCH -------")
    question = state["question"]
    retriever_tavilty = state['runnable']['web_search']

    # Web search retriever
    web_results = retriever_tavilty.invoke(question)

    return {"documents": web_results, "question": question}
