import logging
import os

def setup_logger(name):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_path = os.path.join(log_dir, f"{name}.log")
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        handler = logging.FileHandler(log_path, mode='w')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

    return logger, log_path