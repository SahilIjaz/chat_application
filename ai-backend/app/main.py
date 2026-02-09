from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agents.rag_agent import run_rag_agent as route_agent  # alias to maintain endpoint name

app = FastAPI()

# Allow your frontend (local + production)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",  # Local backend
]

# Add production Vercel URLs
import os
frontend_url = os.getenv("FRONTEND_URL", "")
if frontend_url:
    origins.append(frontend_url)

# Allow any Vercel deployment (optional, more permissive)
origins.extend([
    "https://*.vercel.app",  # All Vercel deployments
])

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # frontend URLs
    allow_credentials=True,
    allow_methods=["*"],    # Allow POST, GET, OPTIONS, etc.
    allow_headers=["*"],
)

@app.post("/agent/run")
async def run_agent(payload: dict):
    message = payload.get("message")
    user_id = payload.get("user_id", "demo_user")
    thread_id = payload.get("thread_id", "default_thread")
    return route_agent(message, user_id, thread_id)
