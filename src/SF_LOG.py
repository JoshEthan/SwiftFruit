import logging

class SF_LOGGER():
    def __init__(self, filename, level):
        logging.basicConfig(filename=filename+'.log', format='[%(asctime)s] %(name)s - %(levelname)s: %(message)s', level=level)

    def DEBUG(self, name, message):
        message = self.checkIfList(message)
        logging.debug("{}: {}".format(name, message))

    def INFO(self, message):
        message = self.checkIfList(message)
        logging.info(message)

    def WARN(self, message):
        message = self.checkIfList(message)
        logging.warning(message)

    def ERROR(self, message):
        message = self.checkIfList(message)
        logging.error(message)

    def checkIfList(self, ini_list1):
        if isinstance(ini_list1, str):
            return ini_list1
        else:
            return vars(ini_list1)
