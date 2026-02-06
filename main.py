from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import generate_project

app = FastAPI(title="Prompt to Production App Builder")


class PromptRequest(BaseModel):
    prompt: str


@app.post("/generate")
def generate_app(req: PromptRequest):
    result = generate_project(req.prompt)
    return {
        "status": "success",
        "details": result
    }
    
@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "auto-app-builder"
    }
    
    
@app.get("/health")
def health():
    return {"status": "ok"}
