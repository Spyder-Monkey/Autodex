import logging
from datetime import datetime

# Create and configure logger
# logging.basicConfig(filename=str(datetime.now())+".log", 
#                     format='%(asctime)s %(filename)s[line:%(lineno)s] %(funcName)s %(levelname)s: %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S',
#                     filemode='w')

logging.basicConfig(filename="logFile.log", 
                    format='%(asctime)s %(filename)s[line:%(lineno)s] %(funcName)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')

def logger():
    logger = logging.getLogger('logger')
    logger.setLevel(logging.INFO)
    return logger