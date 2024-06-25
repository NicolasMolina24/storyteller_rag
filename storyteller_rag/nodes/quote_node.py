import random

CATEGORIES = ["age", "alone", "amazing", "anger", "architecture", "art", "attitude",
              "beauty", "best", "birthday", "business", "car", "change",
              "communication", "computers", "cool", "courage", "dad", "dating",
              "death", "design", "dreams", "education", "environmental", "equality",
              "experience", "failure", "faith", "family", "famous", "fear", "fitness", "food",
              "forgiveness", "freedom", "friendship", "funny", "future", "god", "good",
              "government", "graduation", "great", "happiness", "health", "history",
              "home", "hope", "humor", "imagination", "inspirational", "intelligence",
              "jealousy", "knowledge", "leadership", "learning", "legal", "life",
              "love", "marriage", "medical", "men", "mom", "money", "morning", "movies", "success"]

def get_quote(state):
    """Given a category, get a quote from the API

    Args:
        state(dict): The current graph state
            Uses the following keys:
                runnable['get_quote']: Runnable to be executed

    Returns:
        The quote

        """
    print("------- GETTOING QUOTE -------")
    quote_agent = state['runnable']['get_quote']

    quote = f"Give me a quote about {random.choice(CATEGORIES)}"
    agent_tool_quote_output = quote_agent.invoke(quote)
    tool_output = eval(agent_tool_quote_output[0]['output'])
    return {"generation": tool_output}
