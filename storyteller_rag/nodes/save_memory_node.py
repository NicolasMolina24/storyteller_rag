from storyteller_rag.utils import set_memory

def save_memory(state):
    """
    Save the memory to the memory store.
    
    Args:
        state: The state to save
    """
    memory = state['memory']
    generation = state['generation']
    set_memory(memory, ai_message=generation)
    return state