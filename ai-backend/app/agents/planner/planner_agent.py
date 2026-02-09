def plan_task(message: str):
    """
    Decides what type of task this is
    """
    if "upload" in message.lower():
        return "tool"
    if "summarize" in message.lower():
        return "llm"
    if "plan" in message.lower():
        return "planner"

    return "llm"
