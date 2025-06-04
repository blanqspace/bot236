import logging
import os


def setup_logger(name: str = "tradingbot", log_file: str | None = None) -> logging.Logger:
    """Set up logger that prints to console and writes to a file."""
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger  # Already configured

    if log_file is None:
        log_file = os.path.join(os.path.dirname(__file__), "..", "logs", "bot.log")

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
