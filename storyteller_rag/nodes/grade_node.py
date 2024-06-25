
def grade(state):
    """Grade document if relevant or not
    
    Args:
        state(dict): The current graph state
            Uses the following keys:
                runnable['grade_documents']: Runnable to be executed
                question: The question or query to be answered


    Returns:
        The grade
    """

    print("------- GRADING DOCUMENT -------")
    docs_to_grade = state["documents"]
    question = state["question"]
    grade_documents = state['runnable']['grade_documents']

    # Grading
    filtered_docs = []
    for doc in docs_to_grade:
        responde_grader = grade_documents.invoke(
            {"document": docs_to_grade, "question": question
             })
        if responde_grader.binary_core == "yes":
            print("--------- RELEVANT DOCUMENT ---------")
            filtered_docs.append(doc)
        else:
            print("--------- NOT RELEVANT DOCUMENT ---------")
            continue
    return {"documents": filtered_docs, "question": question}