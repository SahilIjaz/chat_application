from app.agents.llm_agent import run_llm_agent

def run_rag_agent(query: str, user_id: str, thread_id: str):
    # Existing memory + RAG code here
    # ...

    # Detect if the query should use a tool
    if "search:" in query.lower() or "email:" in query.lower() or "sql:" in query.lower():
        tool_response = run_llm_agent(query)
        add_message(user_id, thread_id, "user", query)
        add_message(user_id, thread_id, "assistant", str(tool_response))
        return tool_response

    # Default RAG + LLM response
    reply = run_llm_agent(prompt)
    add_message(user_id, thread_id, "user", query)
    add_message(user_id, thread_id, "assistant", reply["reply"])
    return reply
