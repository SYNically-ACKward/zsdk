"""zsdk Python Package"""

import logging
import sys

from .zia import zia

__author__ = "Ryan Ulrick"
__contributors__ = []
__license__ = "MIT"

__all__ = [
    "zia",
    "zpa",
    "zdx",
]

logging.getLogger(__name__).addHandler(logging.NullHandler())


def add_stderr_logger(
    level: int = logging.DEBUG,
    stream_channel: sys.stderr or sys.stdout = sys.stderr,
) -> logging.StreamHandler:
    """
    Helper for quickly adding a StreamHandler to the logger. Useful for
    debugging.

    Returns the handler after adding it.
    """

    # This method needs to be in this __init__.py to get the __name__ correct.
    name = "zsdk"
    logger = logging.getLogger(name)
    handler = logging.StreamHandler(stream=stream_channel)
    handler.addFilter(logging.Filter(name=name))
    formatter = logging.Formatter(
        fmt="{asctime} {name}.{funcName} {levelname} {message}",
        datefmt="%Y%m%d %H:%M:%S",
        style="{",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(level)
    logger.addFilter(logging.Filter(name=name))
    logger.info(f"Added a streamHandler to logger for the {name} package.")
    return handler


# Clean up.
del logging.NullHandler
