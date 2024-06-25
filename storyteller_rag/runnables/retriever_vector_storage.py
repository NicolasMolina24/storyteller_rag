
def vector_storage_as_retreiver(vector_storage):
    """Vector storage as retriever
    
    Args:
        vector_storage: The vector storage
    
    Returns:
        The vector storage as retriever"""
    return vector_storage.as_retriever()
