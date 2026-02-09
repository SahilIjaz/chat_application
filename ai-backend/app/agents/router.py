from app.agents.rag_agent import run_rag_agent

def route_agent(message: str, user_id="demo_user"):
    if "document" in message.lower():
        return run_rag_agent(message, user_id)

    return run_llm_agent(message)
