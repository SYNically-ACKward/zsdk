import logging
import json
import sys


class StructuredLogger:
    def __init__(self, name, log_level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)

        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter("%(message)s")
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, level, message, **kwargs):
        log_entry = {"level": level, "message": message, **kwargs}
        self.logger.log(level, json.dumps(log_entry))

    def info(self, message, **kwargs):
        self.log(logging.INFO, message, **kwargs)

    def warning(self, message, **kwargs):
        self.log(logging.WARNING, message, **kwargs)

    def error(self, message, **kwargs):
        self.log(logging.ERROR, message, **kwargs)

    def debug(self, message, **kwargs):
        self.log(logging.DEBUG, message, **kwargs)
