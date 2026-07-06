from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level:<8} | {message}",
    level="INFO",
)

logger.add(
    "logs/datarise.log",
    rotation="10 MB",
    retention="7 days",
    level="INFO",
)

def get_logger():
    return logger