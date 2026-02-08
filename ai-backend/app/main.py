from fastapi import FastAPI

app = FastAPI(title="Omni-Agent AI Engine")

@app.get("/")
def health_check():
    return {"status": "ok", "service": "omni-agent"}
