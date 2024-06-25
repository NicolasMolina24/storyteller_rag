# Storytelling RAG

This project develops a RAG (Retrieve-Augment-Generate) with the objective of implementing an interactive and enriching system. Integrate advanced conversational AI using LangChain and Langgraph, enabling coherent user interactions. Enhance responses through the RAG technique, supported by a document database for real-time information retrieval. Maintain conversational context with a persistent memory system, and enrich interactions by integrating external APIs for additional data.

The project consists of four main flows and several key features:

![image.jpeg](imgs\graph.jpeg)
### Main Flows

1. **Retrieve**: Retrieves data from vector storage.
2. **Web Search**: Performs a search using the Tavily API.
3. **Memory History**: Responds to queries about the conversation history.
4. **Get Quote**: Queries the APININJA API to generate a random quote and subsequently creates a fun story based on this quote.



## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Documentation](#documentation)
- [Authors](#authors)
- [Project Status](#project-status)

## Requirements
1.  Create the `.env` file. This file should contain the following API keys:

    - [OPENAI_API_KEY](https://openai.com/index/openai-api/)
    - [TAVILY_API_KEY](https://app.tavily.com/sign-in)
    - [APININJA_KEY](https://api-ninjas.com/register)

    ```sh
    OPENAI_API_KEY = "YOUR API KEY HERE"
    TAVILY_API_KEY = "YOUR API KEY HERE"
    APININJA_KEY = "YOUR API KEY HERE" 
    ```


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/username/project.git
    ```
2. Navigate to the project directory:
    ```sh
    cd project
    ```
3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```


## Usage

Run the application:

    
```python
    # import the create_state_data, create_app objects
    from main import create_state_data, create_app
    # create_app: creates the workflow
    app = create_app()
    # create_state_data: creates a template for the rag state
    state = create_state_data()

    # update key question in the state dict
    state['question'] = "can you give me a summary of what we have discussed? "
    response = app.invoke(state)
    # print the response
    print(response['generation'])
```

## Documentation
```python
    from main import create_state_data
    state = create_state_data()
```
note that the state object always has the following keys:
```
question: question or query to be answered by the llm.
generation: generation resulting from the llm
documents: list of documents used in the graph
memory: list of messages of the session
```

to use the rag the `question` key of the state dictionary must be updated and the app must be invoked. 
```python
    from main import create_state_data
    state = create_state_data()
    # update key question in the state dict
    state['question'] = "can you give me a summary of what we have discussed? "
    response = app.invoke(state)
```
to obtain the llm generation, you must access through the  `generation` key.
```python 
    # print the response
    print(response['generation'])
```

## Autores

- **Nicolás Alberto Molina** - *Trabajo inicial* - [NicolasMolina24](https://github.com/NombreUsuario)