from dotenv import load_dotenv
load_dotenv()

#Step1: Setup API Keys
import os
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

#Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langgraph.prebuilt import create_react_agent

def get_response_from_ai_agent(llm_id, query_messages, allow_search, system_prompt_str, provider):
    """
    This is the core agent logic that connects to the LLM.
    """
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)

    tools=[TavilySearch(max_results=2)] if allow_search else []
    
    messages_list = [SystemMessage(content=system_prompt_str)]
    for msg in query_messages:
        messages_list.append(HumanMessage(content=msg))
        
    agent=create_react_agent(
        model=llm,
        tools=tools,
    )
    
    state={"messages": messages_list}
    response=agent.invoke(state)
    
    # --- YAHAN SABSE ZAROORI BADLAV HAI ---
    # Jawab nikalne ka tareeka aur behtar kiya gaya hai taaki code crash na ho
    response_messages = response.get("messages", [])
    
    final_answer = "No valid response found in the agent's final state."
    if response_messages:
        # Agent ka aakhri message hi uska final jawab hota hai
        last_message = response_messages[-1]
        if hasattr(last_message, 'content'):
            final_answer = last_message.content
    
    return {"response": final_answer}

# This block is for testing this file directly
if __name__ == "__main__":
    # Is block ko aap alag se test karne ke liye use kar sakte hain
    pass