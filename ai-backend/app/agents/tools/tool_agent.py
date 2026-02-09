# Each tool takes params as dict and returns dict

def web_search_tool(params: dict):
    query = params.get("query")
    # For simplicity, use a fake search
    # Later you can integrate Serper/Tavily API
    results = [
        {"title": "Search Result 1", "url": "https://example.com/1"},
        {"title": "Search Result 2", "url": "https://example.com/2"}
    ]
    return {"results": results}


def send_email_tool(params: dict):
    to = params.get("to")
    subject = params.get("subject")
    body = params.get("body")
    # For testing, just log
    print(f"Sending email to {to} | Subject: {subject} | Body: {body}")
    return {"status": "email_sent"}


def db_query_tool(params: dict):
    sql = params.get("sql")
    # For simplicity, return dummy result
    print(f"Executing SQL: {sql}")
    return {"result": [{"id": 1, "name": "Example"}]}
