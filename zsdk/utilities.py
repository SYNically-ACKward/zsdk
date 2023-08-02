import time

import requests
import urllib3
from .logger import setup_logger

# Disable the InsecureRequestWarning
urllib3.disable_warnings(
    category=urllib3.exceptions.InsecureRequestWarning
)

logger = setup_logger(name=__name__)


def get_user_agent() -> str:
    return (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36"
    )


def _request(
    session: requests.Session,
    method: str,
    url: str,
    retries: int = 10,
    wait_time: float = 5,
    silence_logs: bool = False,
    verify: bool = False,
    **kwargs,
) -> requests.Response:
    for attempt in range(retries + 1):
        try:
            result = session.request(method=method.upper(), url=url, **kwargs)
            result.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
            return result
        except requests.RequestException as e:
            if not silence_logs:
                logger.error(f"Encountered error: {e}")
            if attempt < retries:
                logger.debug(f"Retrying request in {wait_time}s. Retries remaining: {retries - attempt}")
                time.sleep(wait_time)
    raise requests.RequestException("Max retries reached")  # Or some other exception, as appropriate
