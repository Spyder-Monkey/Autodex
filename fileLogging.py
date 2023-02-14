import logging
import sys

# Create and configure logger
logging.basicConfig(filename="logFile.log", 
                    format='%(asctime)s %(filename)s[line:%(lineno)s] %(funcName)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filemode='w')

def logger():
    logger = logging.getLogger('logger')
    logger.setLevel(logging.INFO)
    # logger.addHandler(logging.StreamHandler(sys.stdout))
    return logger