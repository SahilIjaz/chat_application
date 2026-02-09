from app.rag.embeddings import embed_text
from app.db.supabase_client import supabase

def search_docs(query: str, user_id: str, limit=5):
    embedding = embed_text(query)

    response = supabase.rpc(
        "match_documents",
        {
            "query_embedding": embedding,
            "match_count": limit,
            "user_id": user_id
        }
    ).execute()

    return response.data
