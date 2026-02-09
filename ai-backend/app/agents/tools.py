"""app/agents/tools.py

Provide simple, synchronous dummy tools used by the example LLM agent.
These are intentionally synchronous to match how `llm_agent.run_llm_agent`
calls them in this project.
"""

def web_search_tool(payload):
    # payload may be a dict or a string
    if isinstance(payload, dict):
        q = payload.get("query") or payload.get("q")
    else:
        q = payload
    return {"result": f"Searching web for: {q}"}


def send_email_tool(payload):
    # payload may be a dict with keys 'to','subject','body' or a tuple/string
    if isinstance(payload, dict):
        to = payload.get("to")
        subject = payload.get("subject")
        body = payload.get("body")
    else:
        # fallback parsing
        to = None
        subject = None
        body = str(payload)
    # dummy send
    print(f"[tools] send_email to={to} subject={subject} body={body}")
    return {"result": "Email sent"}


def db_query_tool(payload):
    if isinstance(payload, dict):
        sql = payload.get("sql") or payload.get("query")
    else:
        sql = payload
    return {"result": f"Result of DB query: {sql}"}
