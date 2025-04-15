import streamlit as st
import logging
import os
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Use backend service name in Docker, otherwise use localhost for local testing
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:8000")  # Inside Docker
# BACKEND_URL = "http://localhost:8000"  # Uncomment for local testing

def main():
    """AI Code Reviewer - Frontend"""
    logger.info("Frontend started")

    st.set_page_config(page_title="AI Code Reviewer", page_icon="🤖", layout="wide")

    st.title("🚀 AI Code Reviewer & Debugger")
    st.write("Analyze, review, and optimize your code with AI-powered insights.")

    # File Upload Section
    uploaded_file = st.file_uploader("Upload your code file", type=["py", "java", "cpp"])
    
    if uploaded_file is not None:
        try:
            # Read file content
            code_content = uploaded_file.getvalue().decode("utf-8")
            st.text_area("📜 Uploaded Code:", code_content, height=250)

            # Send code for analysis
            if st.button("Analyze Code"):
                logger.info("Sending code for analysis")
                response = analyze_code(code_content)
                
                if response:
                    st.success("✅ Analysis Complete")
                    st.json(response)
                else:
                    st.error("❌ Failed to analyze code. Please try again.")
        except Exception as e:
            logger.error(f"Error processing file: {e}")
            st.error("An error occurred while reading the file.")

def analyze_code(code):
    """Send code to FastAPI backend for AI analysis"""
    try:
        response = requests.post(f"{BACKEND_URL}/analyze", json={"code": code})
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to connect to backend: {e}")
        return None

if __name__ == "__main__":
    main()
