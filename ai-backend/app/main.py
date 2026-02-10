import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

# Import your agent logic
# Ensure an __init__.py exists in ai-backend/app and ai-backend/app/agents
from app.agents.rag_agent import run_rag_agent as route_agent

app = FastAPI(title="AgentFlow AI Backend")

# 1. Enhanced CORS Configuration
# Using ["*"] is most reliable for Vercel's dynamic preview URLs
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Request Schema
class AgentRequest(BaseModel):
    message: str
    user_id: Optional[str] = "demo_user"
    thread_id: Optional[str] = "default_thread"

# 3. Health Check (Useful for verifying deployment)
@app.get("/api/health")
async def health_check():
    return {
        "status": "online",
        "version": "1.0.0",
        "environment": os.getenv("VERCEL_ENV", "development")
    }

# 4. Main Agent Endpoint
# Path updated to /api/agent/run to match vercel.json rewrites
@app.post("/api/agent/run")
async def run_agent(payload: AgentRequest):
    try:
        # Pass data to your RAG agent logic
        response = route_agent(
            payload.message, 
            payload.user_id, 
            payload.thread_id
        )
        return response
    except Exception as e:
        print(f"Error running agent: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

# For local development
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)