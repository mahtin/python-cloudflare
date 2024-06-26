""" Logging for Cloudflare API"""
import logging

# try:
#     import http.client as http_client
# except ImportError:
#     # Python 2
#     import httplib as http_client

DEBUG = 0
INFO = 1

class CFlogger():
    """ Logging for Cloudflare API"""

    logger = None
    request_logger = None

    def __init__(self, level):
        """ Logging for Cloudflare API"""
        self.logger_level = self._get_logging_level(level)
        # logging.basicConfig(level=self.logger_level)
        if CFlogger.request_logger is None:
            CFlogger.request_logger = logging.getLogger("requests.packages.urllib3")
            CFlogger.request_logger.setLevel(self.logger_level)
            CFlogger.request_logger.propagate = level

    def getLogger(self):
        """ Logging for Cloudflare API"""
        # create logger
        if CFlogger.logger is None:
            CFlogger.logger = logging.getLogger('Python Cloudflare API v4')
            CFlogger.logger.setLevel(self.logger_level)

            ch = logging.StreamHandler()
            ch.setLevel(self.logger_level)

            # create formatter
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            # add formatter to ch
            ch.setFormatter(formatter)

            # add ch to logger
            CFlogger.logger.addHandler(ch)

            # http_client.HTTPConnection.debuglevel = 1

        return CFlogger.logger

    def _get_logging_level(self, level):
        """ Logging for Cloudflare API"""
        if level is True:
            return logging.DEBUG
        return logging.INFO
