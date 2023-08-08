import time

import requests
import urllib3
from .logger import setup_logger

# Disable the InsecureRequestWarning
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

logger = setup_logger(name=__name__)


def call(
    session: requests.Session,
    method,
    url,
    retries: int = 5,
    wait_time: int = 5,
    silence_logs: bool = False,
    verify: bool = False,
    **kwargs,
):
    for attempt in range(retries + 1):
        try:
            result = session.request(method=method.upper(), url=url, **kwargs)
            result.raise_for_status()
            return result
        except requests.RequestException as e:
            if not silence_logs:
                logger.error(f"Encountered Error: {e}")
            if attempt < retries:
                logger.debug(
                    f"Retrying request in {wait_time}s. Retries remaining: {retries - attempt}"
                )
                time.sleep(wait_time)
    raise requests.RequestException("Max Retries Reached.")


def snake_to_camel(snake_str):
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])
