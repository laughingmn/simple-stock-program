import logging

logger = logging.getLogger(__name__)

# Set the default log level to WARNING, which will suppress INFO and DEBUG messages by default
logger.setLevel(logging.WARNING)  # Or any level you want

# Create a console handler and set its level to WARNING (to match the logger)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)
