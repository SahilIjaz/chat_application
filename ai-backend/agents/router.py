from fastapi import APIRouter
from pydantic import BaseModel
from agents.llm_agent import run_llm_agent

router = APIRouter(prefix="/agent", tags=["Agent Hub"])

class AgentRequest(BaseModel):
    message: str
    agent_type: str = "general"


@router.post("/run")
def run_agent(payload: AgentRequest):

    if payload.agent_type == "llm":
        result = run_llm_agent(payload.message)
    else:
        result = {"reply": "Unknown agent type"}

    return {
        "status": "success",
        "agent_used": payload.agent_type,
        "response": result
    }
