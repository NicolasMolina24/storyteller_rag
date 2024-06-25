from langchain import hub

vector_storage_info = """
    The vectorstore contains documents related to artificial 
    intelligence and machine learning. It is a good source of 
    information for these topics.
    """


route_question = f"""
    You are an expert at routing a user question to a 
    vectorstore, web search, telling a story if the user wants or retrieve
    information about the conversation history. 
    {vector_storage_info}  Use the vectorstore to answer 
    questions related to these topics or the memory for retrieve information about our conversation history. Otherwise, use web search 
    to find the answer. Finally, if the user wants to hear a story, tell a story from a quote."
    """

memory_history = "You are an excellent assistant who obtains accurate information from a chat history"

grade = """
    You are an expert at grading the relevance of documents to a user 
    question,  you can also use the metadata of the document.
    If the document contains keyword(s) or semantic meaning 
    related to the question.
    grade it as 'yes'. Otherwise, grade it as 'no'.
    """

generate = hub.pull("rlm/rag-prompt")

storyteller = """
    you are a famous writer specialized in making the best short stories and you are challenged to come up with the best version of the following: 

    "create a captivating story from the next quote. "

    """

PROMPTS = {
    "route_question": route_question,
    "memory_history": memory_history,
    "grade": grade,
    "generate": generate,
    "storyteller": storyteller,

}