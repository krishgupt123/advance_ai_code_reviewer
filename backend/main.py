from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CodeRequest(BaseModel):
    code: str
    language: str

@app.post("/analyze")
async def analyze_code(request: Request, payload: CodeRequest):
    logger.info(f"Received request: {await request.json()}")  # Log request body

    if not payload.code.strip():
        raise HTTPException(status_code=400, detail="Empty code submitted")

    return {
        "message": "Code analyzed successfully",
        "suggestions": ["Improve variable names", "Optimize loops"],
        "security_issues": ["Possible SQL injection"],
    }
