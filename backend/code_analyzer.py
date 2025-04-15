import logging
from fastapi import APIRouter, HTTPException
import google.generativeai as genai
import os

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Load API Key from environment variable
GEMINI_API_KEY = os.getenv("AIzaSyB0fmBalqm8rQp-UetPimImYNcpObJEX70")

if not GEMINI_API_KEY:
    logger.warning("Gemini API key is missing. Set GEMINI_API_KEY as an environment variable.")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

@router.post("/analyze-code")
def analyze_code(code_snippet: str, language: str = "Python"):
    """Uses AI to analyze code for issues, optimizations, and best practices."""
    try:
        logger.info(f"Analyzing {language} code...")
        
        model = genai.GenerativeModel("gemini-pro")  # Use "gemini-pro" or "gemini-pro-vision" if needed
        response = model.generate_content(
            f"Analyze the following {language} code for bugs, optimizations, and best practices:\n\n{code_snippet}"
        )
        
        analysis_result = response.text if response else "Failed to generate analysis results."
        logger.info("Code analysis completed successfully.")

        return {"analysis": analysis_result}
    
    except Exception as e:
        logger.error(f"Error during code analysis: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to analyze code.")
