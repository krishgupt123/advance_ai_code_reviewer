import logging
from fastapi import APIRouter, HTTPException
from zapv2 import ZAPv2
import os
import time

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# OWASP ZAP Configuration
ZAP_URL = os.getenv("ZAP_URL", "http://localhost:8080")  # Default to local ZAP instance
zap = ZAPv2(proxies={"http": ZAP_URL, "https": ZAP_URL})

@router.get("/security/scan")
def run_security_scan(target_url: str):
    """Performs a security scan using OWASP ZAP on the given target URL."""
    try:
        logger.info(f"Starting OWASP ZAP security scan for {target_url}")

        # Start Passive Scan
        zap.urlopen(target_url)
        time.sleep(2)  # Give ZAP time to process

        # Start Active Scan
        scan_id = zap.ascan.scan(target_url)
        while int(zap.ascan.status(scan_id)) < 100:  # Wait until scan completes
            logger.info(f"Scan in progress... {zap.ascan.status(scan_id)}% completed")
            time.sleep(5)

        logger.info("Security scan completed successfully.")

        # Get results
        alerts = zap.core.alerts()
        return {"message": "Security scan completed", "alerts": alerts}

    except Exception as e:
        logger.error(f"Error running security scan: {str(e)}")
        raise HTTPException(status_code=500, detail="Security scan failed.")
