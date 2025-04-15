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

@router.post("/generate-docs")
def generate_docs(code_snippet: str):
    """Generates docstrings for a given code snippet using Gemini Flash."""
    try:
        logger.info("Generating documentation for the given code snippet...")
        
        model = genai.GenerativeModel("gemini-pro")  # Use "gemini-pro" or "gemini-pro-vision" if needed
        response = model.generate_content(
            f"Generate proper docstrings for the following Python code:\n\n{code_snippet}"
        )
        
        docstring = response.text if response else "Failed to generate docstring."
        logger.info("Documentation generated successfully.")

        return {"generated_docstring": docstring}
    
    except Exception as e:
        logger.error(f"Error generating documentation: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate documentation.")
