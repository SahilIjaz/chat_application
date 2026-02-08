from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Omni-Agent AI Engine")

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "service": "omni-agent",
        "env": os.getenv("ENV")
    }
