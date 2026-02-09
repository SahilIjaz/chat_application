# app/agents/tools.py

async def web_search_tool(query: str):
    # dummy implementation
    return f"Searching web for: {query}"

async def send_email_tool(to_email: str, subject: str, body: str):
    # dummy implementation
    print(f"Sending email to {to_email}: {subject}\n{body}")
    return "Email sent"

async def db_query_tool(query: str):
    # dummy implementation
    return f"Result of DB query: {query}"
