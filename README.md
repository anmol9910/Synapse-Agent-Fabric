🚀 Synapse-Agent-Fabric

🤖 Your Production-Ready Personal Agentic AI Chatbot

Synapse-Agent-Fabric is an advanced, production-grade GenAI application built on a cutting-edge agentic architecture.
It empowers users to create custom AI agents, seamlessly switch between multiple LLM providers (like Groq and OpenAI), and even enable real-time web search to fetch live information.

This modular and scalable system is designed for performance, flexibility, and ease of use, making it perfect for developers, researchers, and AI enthusiasts.

🧩 System Overview
The project is built on a clean three-tier architecture, ensuring a clear separation of concerns and making the system easy to maintain and scale.

1️⃣ Core AI Agent (LangGraph) – The intelligent engine that powers your AI chatbot, capable of reasoning and using tools.

2️⃣ Backend Server (FastAPI) – A high-performance API layer that serves as the bridge between the user interface and the core AI agent.

3️⃣ User Interface (Streamlit) – A sleek, interactive web application designed for an effortless and intuitive user experience.

✨ Key Features

✅ Custom Agent Behavior – Easily configure your agent with a system prompt to define its persona and expertise (e.g., “You are a world-class Financial Analyst”).

✅ Multi-LLM Support – Natively supports switching between Groq's lightning-fast models for speed and OpenAI’s powerful models for capability.

✅ Dynamic Model Selection – Choose the best model for your task on the fly, with options like llama3-8b-8192, gemma-7b-it, gpt-4o-mini, and more.

✅ Real-Time Web Search – Empower your agent to access live internet data using the integrated Tavily Search API.

✅ Scalable & Robust Architecture – Built with modern tools like LangGraph and FastAPI, ensuring stability, flexibility, and scalability.

✅ Modern & Clean UI – A minimal and user-friendly interface designed with Streamlit for a great user experience.

🛠️ Tech Stack
Layer

Tools & Technologies

AI Agent

Python, LangChain, LangGraph (ReAct Agent)

Backend

FastAPI, Uvicorn, Pydantic

Frontend

Streamlit

LLM Providers

Groq, OpenAI

Web Search

Tavily Search API

🏗️ Architecture & Layout
This project is designed with modularity in mind, making it easy to understand, maintain, and extend.

📂 Phase 1: Core AI Agent (ai_agent.py)
This module contains the core intelligence of the application. It uses LangGraph to create a ReAct (Reasoning and Acting) agent that can use tools to answer questions.

📂 Phase 2: Backend Server (backend.py)
This is a FastAPI-powered REST API that exposes a single endpoint for the frontend to communicate with. It uses Pydantic for data validation and acts as a controller, passing requests to the AI agent.

📂 Phase 3: User Interface (frontend.py)
A user-friendly web app built with Streamlit. It provides UI components for model selection, agent customization, and a chat interface for executing queries.

🚀 Getting Started
Follow these steps to get the Synapse-Agent-Fabric running on your local machine.

1️⃣ Prerequisites
Python 3.8+

An IDE like VS Code

2️⃣ Clone the Repository
git clone [https://github.com/your-username/synapse-agent-fabric.git](https://github.com/your-username/synapse-agent-fabric.git)
cd synapse-agent-fabric

3️⃣ Install Dependencies
Create a requirements.txt file with the following content:

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

Then, run the installation command:

pip install -r requirements.txt

4️⃣ Configure API Keys
In your project root directory, create a .env file and add your API keys:

GROQ_API_KEY="gsk_xxxxxxxxxxxxxxxxxxxxxx"
TAVILY_API_KEY="tvly-xxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxx"

5️⃣ Run the Application
Terminal 1: Start the Backend Server
python backend.py

The server will be running at http://127.0.0.1:9999.

Terminal 2: Start the Frontend Application
streamlit run frontend.py

Your chatbot UI will automatically open in a new browser tab.


🎯 Why Synapse-Agent-Fabric?
⚡ Lightning-Fast Inference: Leverage Groq's LPU Inference Engine for near-instant responses.


🌍 Live Web Search: Break free from outdated knowledge with real-time web search capabilities.

🧩 Plug-and-Play Modularity: The decoupled architecture makes it easy to add new features, models, or tools.

🛠️ Developer-Friendly Design: Clean, commented, and well-structured code that is easy to understand and build upon.

Start building your own agent-powered GenAI ecosystem today! 🚀
