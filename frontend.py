from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

system_prompt = st.text_area("Define your AI Agent: ", height=70, placeholder="Act as a helpful AI assistant...")

# Latest working models
MODEL_NAMES_GROQ = ["qwen/qwen3-32b", "gemma2-9b-it", "llama3-8b-8192"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select Provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select OpenAI Model:", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")
user_query = st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")

API_URL = "http://127.0.0.1:9999/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        with st.spinner("Agent soch raha hai..."):
            payload = {
                "model_name": selected_model,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages": [user_query],
                "allow_search": allow_web_search
            }
            try:
                response = requests.post(API_URL, json=payload, timeout=120)
                if response.status_code == 200:
                    response_data = response.json()
                    st.subheader("Agent Response")
                    final_answer = response_data.get("response", "Sorry, I couldn't get a response.")
                    st.markdown(final_answer)
                else:
                    st.error(f"Error from backend: Status {response.status_code}")
                    st.error(f"Details: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error("Backend se connect nahi ho paa raha hai. Kya aapka backend server chal raha hai?")