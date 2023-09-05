import logging

'''
    Logging levels
    
    DEBUG
    INFO
    WARNING
    ERROR
    CRITICAL

'''

logging.basicConfig(level=logging.INFO)

logging.debug("This is not going to output because level configured to INFO")
logging.info("This is an info log")