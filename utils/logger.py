import logging

def setup_logger():
    """Configure logger for the project."""
    logger = logging.getLogger("web_scraper")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    file_handler = logging.FileHandler("web_scraper.log")
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger
