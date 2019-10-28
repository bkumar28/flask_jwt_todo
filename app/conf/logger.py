import logging

from logging import FileHandler


class LoggerFileHandler(object):

    @classmethod
    def create_logger_file_handler(cls, service_tag, logger_filename="application.log"):

        formatter = logging.Formatter(service_tag + "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
        # Log filename should be taken from app config. Also, can be redirected to SysLog
        file_handler = FileHandler(filename=logger_filename)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        return file_handler
