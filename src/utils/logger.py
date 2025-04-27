import logging

logger = logging.getLogger(__name__)

# Set the default log level to WARNING, which will suppress INFO and DEBUG messages by default
logger.setLevel(logging.WARNING)  # Or any level you want

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
