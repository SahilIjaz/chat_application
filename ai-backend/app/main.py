from fastapi import FastAPI
from app.services.supabase_client import supabase

app = FastAPI(title="Omni-Agent AI Engine")

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/db-test")
def db_test():
    data = supabase.table("documents").select("*").execute()
    return {"rows": len(data.data)}
