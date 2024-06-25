from storyteller_rag.utils import set_memory


def route_question(state):
    """
    Route the question to web search, vectorstore, storyteller or memory

    Args:
        state(dict): The current graph state
            Uses the following keys:
                question: The question or query to be answered
                memory: The list of messages in the session
                runnable: Runnables to be executed

    Returns:
        str: Next node to call
    """

    print("----ROUTE QUESTION----")
    question = state["question"]
    memory = state["memory"]
    query_router = state["runnable"]["query_router"]
    # Save the question to the memory
    print("----saving memory----")
    set_memory(memory, user_message=question)
    print("----ROUTE QUESTION----")
    source = query_router.invoke({"question": question})
    out = 'None'
    if source.route == "web_search":
        print("----ROUTE QUESTION: Web search")
        out = "web_search"
    elif source.route == "vectorstore":
        print("----ROUTE QUESTION: Vectorstore")
        out = "retrieve"
    elif source.route == "storyteller":
        print("----ROUTE QUESTION: Storyteller")
        out = "get_quote"
    elif source.route == "memory":
        print("----ROUTE QUESTION: Memory")
        out = "memory_history"
    return out
