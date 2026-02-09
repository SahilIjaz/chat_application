from app.agents.tools import web_search_tool, send_email_tool, db_query_tool

TOOLS = {
    "web_search": web_search_tool,
    "send_email": send_email_tool,
    "db_query": db_query_tool
}

def run_llm_agent(prompt: str):
    """
    Simulate Groq LLM response that may call a tool.
    """
    # For demonstration: if prompt contains a keyword, call the tool
    if "search:" in prompt.lower():
        query = prompt.split("search:")[1].strip()
        return web_search_tool({"query": query})

    if "email:" in prompt.lower():
        parts = prompt.split("email:")[1].strip().split("|")
        to = parts[0].strip()
        subject = parts[1].strip()
        body = parts[2].strip()
        return send_email_tool({"to": to, "subject": subject, "body": body})

    if "sql:" in prompt.lower():
        sql = prompt.split("sql:")[1].strip()
        return db_query_tool({"sql": sql})

    # Default: just reply with Groq LLM output
    return {"reply": f"LLM reply based on prompt: {prompt}"}
