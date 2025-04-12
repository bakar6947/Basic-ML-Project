import os
import logging
from datetime import datetime


LOG_FILE = f'{datetime.now().strftime("%d-%m-%y-%H-%M-%S")}.log'
log_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(log_path, exist_ok=True)


LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)
FILE_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

logging.basicConfig(
    filename = LOG_FILE_PATH,
    level = logging.INFO,
    format = FILE_FORMAT,
    datefmt = "%Y-%m-%d %H:%M:%S",
)


# Test Logging
if __name__ == "__main__":
    logging.info("Logging has started")