# AI Documentation assistant Project ✅
![Blog Image](https://raw.githubusercontent.com/excommunicades/ai-document-assistant/master/Preview.png)

## DESCRIPTION: 

Documentation Assistant is an AI-powered REST API built with FastAPI. It processes .txt documents from /docs, creates embeddings with HuggingFace, and stores them in Weaviate for semantic search.
When a user asks a question, the system retrieves relevant text chunks and uses Ollama (via LangChain) to generate an answer.

The architecture is modular, scalable, and fully local, making it easy to integrate with other apps while keeping data private.

## STACK: 

Python3, FastAPI, LangChain, OllamaLLM (mistral:7b), Hugging Face (sentence_transformers), Weaviate, Pydantic, Uvicorn, etc...

## This project demonstrates how to integrate Large Language Models (LLMs) into a custom REST API using FastAPI. The code serves as a practical guide to the following concepts:

* **FastAPI Web Server: Set up a lightweight and efficient REST API for AI-powered applications.**
* **Document Ingestion: Load and process files .txt from a /docs directory for AI use.**
* **Text Chunking: Split documents into manageable pieces for better embeddings and retrieval.**
* **Embeddings with HuggingFace: Generate semantic vector representations of text chunks.**
* **Vector Database with Weaviate: Store and retrieve document embeddings for similarity search.**
* **LLM Integration with Ollama and LangChain: Use local large language models to answer user questions based on retrieved document context.**
* **Configurable Settings: Manage environment variables (paths, model APIs) via Pydantic Settings.**

## Key Features 💡

- **FastAPI Web Server:** Provides a lightweight and high-performance REST API framework for handling user queries.  
- **Document Ingestion Pipeline:** Automatically loads and processes .txt documents from a /docs directory.  
- **Text Chunking & Embeddings:** Splits documents into chunks and generates semantic embeddings using HuggingFace models.  
- **Vector Database with Weaviate:** Stores embeddings for efficient similarity search and document retrieval.  
- **LLM Integration via LangChain & Ollama:** Uses local large language models to generate answers strictly based on retrieved context.  
- **Configurable Settings:** Manages environment variables (paths, APIs, etc.) with Pydantic Settings.  
- **Modular & Scalable Architecture:** Ensures clean project structure, easy maintenance, and future extensibility

# Installation Guide 📕:

### Prerequisites 💻

Ensure you have Docker and Docker Compose installed on your machine. You can download them from:

- Docker: [Get Docker](https://docs.docker.com/get-docker/) 🐳
- Docker Compose: [Docker Compose](https://docs.docker.com/compose/install/) 🐳

### Environment Variables
Create a `.env` file in the root of your project directory with the following content:
```
# PROJECT

APP_ENV=development
APP_DEBUG=True
DOCS_PATH=app/docs

# LOCAL LLM

OLLAMA_API=http://ollama:11434
LLM_MODEL=mistral:7b # You can set your own

# WEAVITE DB

WEAVIATE_URL=http://weaviate:8080
WEAVIATE_CLASS_NAME=Documents
```

# Start the Services 🚪

1. **Clone the repository:** ```git clone https://github.com/excommunicades/ai-document-assistant.git``` -> ```cd ai-document-assistant```
2. **Create `.env` file**
3. **Build and run the application with Docker Compose:** ```docker-compose up --build```
4. **Pull LLM Model to ollama while ollama docker container is running:** ```docker exec ollama ollama pull mistral:7b```

# Stopping the Services 🚪

**To stop all running services, you can use:** ```docker-compose down```

### API Endpoints

#### AI

- **POST** /ai/prompt: Accepts a user query, retrieves relevant document chunks from Weaviate, builds a context, and generates an AI-powered answer using Ollama LLM. Returns a response based on documents.

#### Manage

- **GET** /manage/health: Check server connection status  

# IMPORTANT ♻️

⚠️ WARNING: PyTorch and HuggingFace models are large in size, so building the FastAPI Docker container can take up to 30 minutes depending on your computer’s performance. Please be patient during the first build.  

If you prefer to run the application directly on your local device instead of inside the Docker container, update your `.env` settings as follows:  

- Change `OLLAMA_API=http://ollama:11434` → `OLLAMA_API=http://localhost:11434`  
- Change `WEAVIATE_URL=http://weaviate:8080` → `WEAVIATE_URL=http://localhost:8080`  
- Change `DOCS_PATH=app/docs` → `DOCS_PATH=/docs` 

Also, make sure to move your `.env` file **out of the `app/` folder** and place it at the project root directory.  

Timely indexing is necessary for the correct operation of the AI assistant for searching products.

# Conclusion

This project was created to demonstrate my desire to adapt and learn new tools, as well as to improve and deepen my expertise in the technologies I already know.

## Authors 😎

- **Stepanenko Daniil** - "Documentation Assistant"