from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.agents.rag_agent import route_agent  # your agent function

app = FastAPI()

# Allow your frontend
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # frontend URL
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
