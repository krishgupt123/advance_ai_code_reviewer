import logging
from fastapi import APIRouter, HTTPException
import requests

router = APIRouter()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

GITHUB_API_URL = "https://api.github.com"

@router.get("/github/review")
def review_github_repo(owner: str, repo: str, token: str):
    """Fetches pull requests for a given GitHub repository and analyzes code changes."""
    headers = {"Authorization": f"token {token}"}
    pr_url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/pulls"

    try:
        response = requests.get(pr_url, headers=headers)
        response.raise_for_status()
        pull_requests = response.json()

        if not pull_requests:
            logger.info(f"No pull requests found for {owner}/{repo}.")
            return {"message": "No pull requests found."}

        logger.info(f"Found {len(pull_requests)} pull requests for {owner}/{repo}.")
        return {"pull_requests": pull_requests}

    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching GitHub data: {e}")
        raise HTTPException(status_code=500, detail="Error fetching GitHub data")
