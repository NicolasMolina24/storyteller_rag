from langchain_core.messages import AIMessage

def storyteller(state):
    """Given a quote create a story
    
    Args:
        state: the current state of the graph

    Returns:
        The story
    """
    print("------- CREATING THE STORY -------")
    quote_info = state["generation"][0]
    storyteller_chain = state['runnable']['storyteller']
    storyteller_out = storyteller_chain.invoke(quote_info)
    storyteller_out = AIMessage(content=storyteller_out.json())
    return {"generation": storyteller_out}