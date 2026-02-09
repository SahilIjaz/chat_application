from app.agents.llm_agent import run_llm_agent


def _safe_add_message(user_id, thread_id, role, content):
    """Call add_message if available in the module scope; otherwise ignore."""
    try:
        add_message(user_id, thread_id, role, content)
    except NameError:
        # optional: log or ignore when add_message isn't implemented
        pass


def run_rag_agent(query: str, user_id: str, thread_id: str):
    # Existing memory + RAG code here
    # ...

    # Detect if the query should use a tool
    if "search:" in query.lower() or "email:" in query.lower() or "sql:" in query.lower():
        tool_response = run_llm_agent(query)
        _safe_add_message(user_id, thread_id, "user", query)
        # normalize tool response into a string
        if isinstance(tool_response, dict):
            resp_text = tool_response.get("reply") or tool_response.get("result") or str(tool_response)
        else:
            resp_text = str(tool_response)
        _safe_add_message(user_id, thread_id, "assistant", resp_text)
        return {"reply": resp_text}

    # Default RAG + LLM response
    reply = run_llm_agent(query)
    _safe_add_message(user_id, thread_id, "user", query)
    # reply may be a dict with 'reply' or a string
    resp_text = reply.get("reply") if isinstance(reply, dict) and "reply" in reply else str(reply)
    _safe_add_message(user_id, thread_id, "assistant", resp_text)
    return {"reply": resp_text}
