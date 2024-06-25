from langchain_community.retrievers import TavilySearchAPIRetriever

def runnable_web_search():
    """Runnable, retrieve for web search.
    This runnable uses the tavily retrieve with 3 results.
    
    Returns:
        The agent chain"""
    return TavilySearchAPIRetriever(k=3)
