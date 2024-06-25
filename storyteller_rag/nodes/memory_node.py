
def memory_history(state):
    """Retrieve the memory
    
    Args:
        state(dict): The current graph state
            Uses the following keys:
                runnable['memory_chain']: Runnable to be executed
                question: The question or query to be answered
        
    Returns:
        The memory anwser
    """
    
    print("---GET MEMORY---")
    history = state["memory"]
    question = state["question"]
    memory_chain = state['runnable']['memory_chain']
    memory_out = memory_chain.invoke(
        {
            "input": question,
            "history": history.messages,
        }
    )
    return {"generation": memory_out.content}