import logging
import subprocess
from fastapi import APIRouter, HTTPException

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

@router.get("/dependencies/audit")
def audit_dependencies():
    """Scans project dependencies for security vulnerabilities."""
    try:
        logger.info("Starting dependency audit using pip-audit...")
        result = subprocess.run(["pip-audit"], capture_output=True, text=True, check=True)
        logger.info("Dependency audit completed successfully.")
        return {"audit_results": result.stdout}
    
    except subprocess.CalledProcessError as e:
        logger.error(f"Dependency audit failed: {e.stderr}")
        raise HTTPException(status_code=500, detail="Dependency security audit failed.")

@router.get("/dependencies/list")
def list_dependencies():
    """Lists installed dependencies."""
    try:
        logger.info("Fetching installed dependencies...")
        result = subprocess.run(["pip", "list"], capture_output=True, text=True, check=True)
        return {"installed_dependencies": result.stdout}
    
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to list dependencies: {e.stderr}")
        raise HTTPException(status_code=500, detail="Failed to fetch dependencies.")
