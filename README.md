# Synapse-Agent-Fabric

🤖 Personal Agentic AI Chatbot (Production Ready)


This is an advanced, production-ready GenAI application built on a powerful agentic architecture. This application allows users to create custom AI agents, choose between different LLM providers (like Groq and OpenAI), and toggle real-time web search capabilities.

The entire system is divided into three distinct parts:

Core AI Agent (LangGraph): This is the brain of the project.

Backend Server (FastAPI): This acts as a bridge between the UI and the AI Agent.

User Interface (Streamlit): This is a clean and interactive web app for user interaction.

✨ Key Features
Custom Agent Behavior: Define the agent's behavior (e.g., "act as a financial analyst") using a System Prompt.

Multiple LLM Providers: Switch between Groq's super-fast models and OpenAI's powerful models.

Dynamic Model Selection: Option to select different models within each provider (e.g., qwen, gemma, gpt-4o-mini).

Real-time Web Search: Empower the agent to search for real-time information on the internet using the Tavily API.

Robust & Scalable Architecture: The FastAPI backend and LangGraph agent make this project stable and scalable.

Interactive UI: A user-friendly interface built with Streamlit.

🛠️ Tools and Technologies
This project was built using the following modern tools and technologies:

![Tools and Technologies]

AI Agent: LangChain & LangGraph (React Agent)

Backend: FastAPI, Uvicorn

Frontend: Streamlit

LLM Providers: Groq, OpenAI

Web Search Tool: Tavily Search

Programming Language: Python

🏗️ Project Architecture & Layout
The project is designed with a 3-phase architecture, making it modular and easy to manage.

![Project Layout]

Phase 1: The Core AI Agent (ai_agent.py)
This is the core engine of the project. It uses LangGraph's create_react_agent, which gives the LLM the ability to use tools (like web search).

Phase 2: The Backend Server (backend.py)
A high-performance API server built with FastAPI. It receives requests from the frontend, validates them with Pydantic, and calls ai_agent.py to return a response to the frontend.

Phase 3: The User Interface (frontend.py)
An interactive web application built with Streamlit. It provides the user with all the options to interact with the AI Agent (model selection, system prompt, etc.).

Architecture Diagram
![Project Architecture Diagram]

📸 Application in Action 
Here's a look at how the application works:

Selecting a model with the Groq Provider:


Creating a specific agent (Financial Analyst) and making a query:


🚀 Getting Started: Setup & Installation
To run this project on your local machine, follow these steps:

1. Install Dependencies
First, install all the necessary Python libraries. Create a requirements.txt file, add the libraries listed below, and run pip install -r requirements.txt.

streamlit
fastapi
uvicorn
python-dotenv
requests
langchain
langchain-groq
langchain-openai
langchain-tavily
langgraph

2. Set Up API Keys
In the root folder of the project, create a file named .env and add your secret API keys:

GROQ_API_KEY="gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxx"
TAVILY_API_KEY="tvly-xxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxx"

Remember to replace xxxx with your actual keys.

3. Run the Application
You will need two separate terminals to run this application.

Terminal 1: Start the Backend Server

python backend.py

This will start your API server at http://127.0.0.1:9999. Leave this terminal running.

Terminal 2: Start the Frontend App

python -m streamlit run frontend.py

This command will open a new tab in your browser where your app will be live.

You are now ready to interact with your Personal Agentic AI Chatbot!
