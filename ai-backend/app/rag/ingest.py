from fastapi import APIRouter, UploadFile, File
from app.rag.embeddings import embed_text
from app.services.supabase_client import supabase  # <-- fixed import
import fitz  # PyMuPDF
import uuid

ingest_router = APIRouter(prefix="/ingest", tags=["Ingest"])

@ingest_router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...), user_id: str = "demo_user"):
    pdf_bytes = await file.read()
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")

    text = ""
    for page in doc:
        text += page.get_text()

    embedding = embed_text(text)

    supabase.table("documents").insert({
        "id": str(uuid.uuid4()),
        "name": file.filename,
        "user_id": user_id,
        "content": text,
        "embedding": embedding
    }).execute()

    return {"status": "stored"}
