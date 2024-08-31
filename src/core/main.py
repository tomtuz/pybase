import logging
import os

from dotenv import load_dotenv

from core.logging_config import setup_logging
from core.utils.helpers import logger


# Load environment variables
load_dotenv()

setup_logging()
log = logging.getLogger(__name__)


def main() -> None:
    log.info("Running main.py")
    log.debug(f"Debug mode: {os.getenv('DEBUG')}")
    log.info(f"API Key: {os.getenv('API_KEY')}")
    log.info(f"Database URL: {os.getenv('DATABASE_URL')}")
    logger()
