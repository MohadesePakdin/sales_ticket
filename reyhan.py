import logging
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename= "info.log",
                     level=logging.INFO,
                     format=LOG_FORMAT)
logging.basicConfig(filename= "info.error",
                     level=logging.ERROR,
                     format=LOG_FORMAT)
logging.basicConfig(filename= "info.warning",
                     level=logging.WARNING,
                     format=LOG_FORMAT)



