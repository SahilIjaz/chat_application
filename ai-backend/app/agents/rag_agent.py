from app.rag.search import search_docs
from app.agents.llm_agent import run_llm_agent

def run_rag_agent(query: str, user_id: str):
    docs = search_docs(query, user_id)

    context = "\n".join([d["content"] for d in docs])

    prompt = f"""
Use the following context to answer the question.

Context:
{context}

Question:
{query}
"""

    return run_llm_agent(prompt)
