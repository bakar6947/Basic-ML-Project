import os
import logging
from datetime import datetime


LOG_FILE = f'{datetime.now().strftime("%d_%m_%y_%H_%M_%S")}.log'

LOG_PATH = os.path.join(os.getcwd(), 'Logs', LOG_FILE)
os.makedirs(LOG_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    level = logging.INFO,
    format = "[ %(asctime)s ] %(lineno)d - %(name)s - %(levelname)s - %(message)s]",
)


# Test Logging
# if __name__ == "__main__":
#     logging.info("Logging has started")