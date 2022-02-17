import inspect
import logging

def customLogger(logLevel=logging.DEBUG):   # le seteo un valor para que, en caso de que no se provea de afuera, tenga un valor de default.
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", mode='a')  # automation.los es el nombre del archivo, y "a" (append) para que se vaya agregando la informaciond e cada log, simo con el "w"(write), cada log de cada archivo me va a ir sobreescribiendo el anterior
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
