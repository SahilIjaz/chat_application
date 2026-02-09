from app.agents.tools import web_search_tool, send_email_tool, db_query_tool
import ast
import operator as op
import re

TOOLS = {
    "web_search": web_search_tool,
    "send_email": send_email_tool,
    "db_query": db_query_tool,
}


# safe eval helpers
ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}


def _safe_eval(node):
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    if isinstance(node, ast.Num):
        return node.n
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp):
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](left, right)
    if isinstance(node, ast.UnaryOp):
        operand = _safe_eval(node.operand)
        op_type = type(node.op)
        if op_type in ALLOWED_OPERATORS:
            return ALLOWED_OPERATORS[op_type](operand)
    raise ValueError("Unsupported expression")


def _extract_math_expression(text: str):
    # Remove common question words and punctuation
    t = text.strip().lower()
    t = re.sub(r"what is |calculate |answer:|please compute |\?", "", t)
    # allow digits, operators, parentheses, spaces, and decimal points
    if re.fullmatch(r"[0-9\s\+\-\*/\.\%\(\)f]+", t.replace(',', '')):
        return t
    # fallback: try to extract a simple expression like '2 + 2' from the text
    m = re.search(r"([0-9\(\)\s\+\-\*/\.\%]+)", text)
    return m.group(1).strip() if m else None


def run_llm_agent(prompt: str):
    """
    Simulate LLM response; handle tool triggers and simple arithmetic directly.
    Returns a dict with a `reply` string.
    """
    if not prompt:
        return {"reply": ""}

    # Attempt to evaluate simple math queries first
    try:
        expr = _extract_math_expression(prompt)
        if expr:
            # parse and evaluate safely
            node = ast.parse(expr, mode="eval")
            result = _safe_eval(node)
            return {"reply": str(result)}
    except Exception:
        # not a math expression or evaluation failed — fall through
        pass

    lowered = prompt.lower()
    # Tool invocations
    if "search:" in lowered:
        query = prompt.split("search:", 1)[1].strip()
        return {"reply": TOOLS["web_search"]({"query": query}).get("result") if isinstance(TOOLS["web_search"]({"query": query}), dict) else str(TOOLS["web_search"]({"query": query}))}

    if "email:" in lowered:
        parts = prompt.split("email:", 1)[1].strip().split("|")
        to = parts[0].strip()
        subject = parts[1].strip() if len(parts) > 1 else ""
        body = parts[2].strip() if len(parts) > 2 else ""
        res = TOOLS["send_email"]({"to": to, "subject": subject, "body": body})
        return {"reply": res.get("result") if isinstance(res, dict) else str(res)}

    if "sql:" in lowered:
        sql = prompt.split("sql:", 1)[1].strip()
        res = TOOLS["db_query"]({"sql": sql})
        return {"reply": res.get("result") if isinstance(res, dict) else str(res)}

    # Default: friendly echo
    return {"reply": f"LLM reply based on prompt: {prompt}"}
