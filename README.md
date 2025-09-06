🚀 Synapse-Agent-Fabric

🤖 Your Production-Ready Personal Agentic AI Chatbot

Synapse-Agent-Fabric is an advanced, production-grade GenAI application built on a cutting-edge agentic architecture. It empowers users to create custom AI agents, seamlessly switch between multiple LLM providers (like Groq and OpenAI), and even enable real-time web search to fetch live information.

This modular and scalable system is designed for performance, flexibility, and ease of use, making it perfect for developers, researchers, and AI enthusiasts.

🧩 System Overview

The project is built on a three-tier architecture, ensuring clear separation of responsibilities:

1️⃣ Core AI Agent (LangGraph) – The intelligent engine powering your AI chatbot.
2️⃣ Backend Server (FastAPI) – The high-performance API layer bridging UI and AI.
3️⃣ User Interface (Streamlit) – A sleek, interactive web application for effortless interaction.

✨ Key Features

✅ Custom Agent Behavior – Configure your agent with a system prompt (e.g., “Act as a Financial Analyst”).
✅ Multi-LLM Support – Switch between Groq’s lightning-fast models and OpenAI’s powerful models.
✅ Dynamic Model Selection – Choose models like qwen, gemma, or gpt-4o-mini on the fly.
✅ Real-Time Web Search – Fetch live internet data with Tavily API integration.
✅ Scalable & Robust Architecture – Built with LangGraph and FastAPI for stability and flexibility.
✅ Modern UI – A clean, minimal, and user-friendly interface designed in Streamlit.

🛠️ Tech Stack
Layer	Tools & Technologies
AI Agent	LangChain, LangGraph (ReAct Agent)
Backend	FastAPI, Uvicorn
Frontend	Streamlit
LLM Providers	Groq, OpenAI
Search Integration	Tavily Search
Language	Python
🏗️ Architecture & Layout

This project is designed with modularity in mind, making it easy to maintain and extend.

📂 Phase 1: Core AI Agent (ai_agent.py)

Implements create_react_agent from LangGraph for tool-using AI agents.

📂 Phase 2: Backend Server (backend.py)

FastAPI-powered REST API.

Uses Pydantic for validation and connects directly to the AI agent.

📂 Phase 3: User Interface (frontend.py)

Streamlit web app for easy interaction.

Provides model selection, agent customization, and query execution.

🖼️ Architecture Diagram

(Insert Architecture Diagram Here)

📸 In Action

🔹 Model Selection (Groq Provider) – Choose a model and start chatting instantly.
🔹 Agent Customization – Build domain-specific agents like Financial Analysts, Data Scientists, or Research Bots.

🚀 Getting Started
1️⃣ Install Dependencies

Create a requirements.txt and install:

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


Then run:

pip install -r requirements.txt

2️⃣ Configure API Keys

In your project root, create a .env file:

GROQ_API_KEY="gsk_xxxxxxxxxxxxxxxxxxxxxx"
TAVILY_API_KEY="tvly-xxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxx"

3️⃣ Run the Application

Terminal 1: Start Backend Server

python backend.py


Server runs at: http://127.0.0.1:9999

Terminal 2: Start Frontend

python -m streamlit run frontend.py


Your chatbot UI will open in a browser tab.

🎯 Why Synapse-Agent-Fabric?

⚡ Lightning-fast inference with Groq models.

🌍 Live web search capability.

🧩 Plug-and-play modularity for scaling.

🛠️ Developer-friendly design with clean architecture.

Start building your own agent-powered GenAI ecosystem today! 🚀
