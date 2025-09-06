from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent
import uvicorn

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

# Latest working models
ALLOWED_MODEL_NAMES = ["qwen/qwen3-32b", "gemma2-9b-it", "llama3-8b-8192", "gpt-4o-mini"]

app = FastAPI(title="LangGraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState): 
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}
    
    response = get_response_from_ai_agent(
        llm_id=request.model_name, 
        query_messages=request.messages, 
        allow_search=request.allow_search, 
        system_prompt_str=request.system_prompt, 
        provider=request.model_provider
    )
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9999)