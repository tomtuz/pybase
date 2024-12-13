import logging
import os
from typing import Any

from dotenv import load_dotenv

from core.logging_config import setup_logging

# Load environment variables
load_dotenv()

# Configure logging
setup_logging()
logger = logging.getLogger(__name__)


def get_config() -> dict[str, Any]:
    """Get configuration from environment variables"""
    return {
        "debug": os.getenv("DEBUG", "false").lower() == "true",
        "api_key": os.getenv("API_KEY"),
        "database_url": os.getenv("DATABASE_URL"),
        "env": os.getenv("ENV", "development"),
    }


def validate_config(config: dict[str, Any]) -> None:
    """Validate configuration and log warnings/errors"""
    env = config["env"]

    # In production, we require certain config values
    if env == "production":
        if not config["api_key"]:
            logger.error("API key is required in production")
            raise ValueError("API key is required in production environment")
        if not config["database_url"]:
            logger.error("Database URL is required in production")
            raise ValueError("Database URL is required in production environment")
    else:
        # In development/staging, we just warn about missing values
        if not config["api_key"]:
            logger.warning("API key not set - some features may be limited")
        if not config["database_url"]:
            logger.warning("Database URL not set - using default local database")


def main() -> None:
    """Main application entry point"""
    try:
        logger.info("Application starting")

        # Load configuration
        config = get_config()
        logger.debug("Configuration loaded", extra={"config": config})

        # Validate configuration based on environment
        validate_config(config)

        if config["debug"]:
            logger.info("Debug mode enabled")

        # Example of structured logging with extra context
        logger.info(
            "Processing request",
            extra={
                "user_id": "example_user",
                "action": "startup",
                "metadata": {"version": "1.0.0"},
            },
        )

        # Example of different log levels
        logger.debug("This is a debug message with technical details")
        logger.info("This is an informational message")
        logger.warning("This is a warning message")

        # Your application logic here
        logger.info("Application running successfully")

    except Exception as e:
        logger.exception("Unexpected error occurred", exc_info=True)
        raise
    finally:
        logger.info("Application shutdown")
