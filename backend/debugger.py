import logging
from fastapi import APIRouter, HTTPException
import google.generativeai as genai
import os

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load API Key from environment variable
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    logger.warning("Gemini API key is missing. Set GEMINI_API_KEY as an environment variable.")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

@router.post("/debug")
def debug_code(code_snippet: str):
    """Uses AI to analyze a code snippet, detect bugs, and suggest fixes."""
    try:
        logger.info("Starting AI-powered debugging...")
        
        model = genai.GenerativeModel("gemini-pro")  # Use "gemini-pro" or "gemini-pro-vision" if needed
        response = model.generate_content(
            f"Find and fix bugs in the following code:\n\n{code_snippet}"
        )
        
        debug_result = response.text if response else "Failed to generate debugging results."
        logger.info("Debugging completed successfully.")

        return {"debugged_code": debug_result}
    
    except Exception as e:
        logger.error(f"Error during debugging: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to analyze code.")
