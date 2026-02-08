from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import fitz  # PyMuPDF
import os
from app.services.supabase_client import supabase

ingest_router = APIRouter(prefix="/ingest", tags=["ingest"])

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@ingest_router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...), user_id: str = "demo_user"):
    file_location = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Read PDF
    pdf_text = ""
    doc = fitz.open(file_location)
    for page in doc:
        pdf_text += page.get_text()

    # Save document metadata in Supabase
    data = supabase.table("documents").insert(
        {
            "name": file.filename,
            "user_id": user_id
        }
    ).execute()

    return JSONResponse(
        {"status": "success", "document_id": data.data[0]["id"], "text_length": len(pdf_text)}
    )
