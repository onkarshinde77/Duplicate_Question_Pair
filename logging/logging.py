import logging
from datetime import datetime
import os


# this is only file name ( for unique name used the current date & time)
# strftime - string format time
LOG_FILE = f"{datetime.now().strftime("%d%m%y%H%M%S")}"

# creating log directory and addiong log file
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename = f"{LOG_FILE_PATH}.log",
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s ",
    level = logging.INFO,
)

