import logging
import os
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path

from colorama import Fore, Style, init
from pythonjsonlogger import jsonlogger

# Initialize colorama for cross-platform color support
init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    """Custom formatter with colored output for console"""

    COLORS = {
        "DEBUG": Fore.BLUE,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.RED + Style.BRIGHT,
    }

    def format(self, record: logging.LogRecord) -> str:
        # Add color to level name if it's one of our defined levels
        if record.levelname in self.COLORS:
            record.levelname = (
                f"{self.COLORS[record.levelname]}{record.levelname}{Style.RESET_ALL}"
            )
        return super().format(record)


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    """Custom JSON formatter with additional fields"""

    def add_fields(
        self, log_record: dict, record: logging.LogRecord, message_dict: dict
    ) -> None:
        super().add_fields(log_record, record, message_dict)
        log_record["app"] = "core-project"
        log_record["environment"] = os.getenv("ENV", "development")


def get_log_level() -> str:
    """Get log level from environment variable or default to INFO"""
    return os.getenv("LOG_LEVEL", "INFO").upper()


def get_log_file() -> Path:
    """Get log file path from environment variable or use default"""
    log_dir = Path(os.getenv("LOG_DIR", "logs"))
    log_dir.mkdir(exist_ok=True)
    return log_dir / "app.log"


def setup_logging() -> None:
    """Configure logging with console and file handlers"""
    log_level = get_log_level()
    log_file = get_log_file()

    # Console handler with colored output (no timestamp)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(log_level)
    console_formatter = ColoredFormatter("[%(levelname)s] %(name)s: %(message)s")
    console_handler.setFormatter(console_formatter)

    # Rotating file handler with JSON formatting (keeps timestamp)
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10 * 1024 * 1024,  # 10MB
        backupCount=5,
        encoding="utf-8",
    )
    file_handler.setLevel(logging.DEBUG)  # Always log debug to file
    file_formatter = CustomJsonFormatter(
        "%(timestamp)s %(level)s %(name)s %(message)s",
        timestamp=True,
    )
    file_handler.setFormatter(file_formatter)

    # Root logger configuration
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # Capture all logs

    # Remove existing handlers
    root_logger.handlers = []

    # Add our handlers
    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)

    # Suppress some noisy loggers
    logging.getLogger("urllib3").setLevel(logging.WARNING)

    # Log startup information
    root_logger.info(
        "Logging configured",
        extra={
            "log_level": log_level,
            "log_file": str(log_file),
            "environment": os.getenv("ENV", "development"),
        },
    )
