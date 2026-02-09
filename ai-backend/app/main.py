from fastapi import FastAPI
from app.services.supabase_client import supabase
from app.rag.ingest import ingest_router
from agents.router import router as agent_router

app = FastAPI(title="Omni-Agent AI Engine")

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/db-test")
def db_test():
    data = supabase.table("documents").select("*").execute()
    return {"rows": len(data.data)}

app.include_router(agent_router)
app.include_router(ingest_router)
