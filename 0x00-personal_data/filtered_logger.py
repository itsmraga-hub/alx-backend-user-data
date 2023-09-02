#!/usr/bin/env python3
"""
    function called filter_datum that returns the log message obfuscated:
"""

import re
import logging
from os import environ
import mysql.connector
from typing import List

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
        function called filter_datum that returns the log message
        obfuscated:
    """
    return re.sub(r'('
                  + '|'.join(fields) + r')=[^{}]*'.format(separator),
                  r'\1=' + redaction, message)


def get_logger() -> logging.Logger:
    """ Returns a Logger Object """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


class RedactingFormatter(logging.Formatter):
    """
        Redacting Formatter class
        Update the class to accept a list of strings fields constructor
        argument.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        log_message = super().format(record)
        return filter_datum(self.fields, self.REDACTION,
                            log_message, self.SEPARATOR)
        # return re.sub(r'(' + '|'.join(self.fields) +
        #               r')=[^{}]*'.format(self.SEPARATOR),
        #               r'\1=' + self.REDACTION, log_message)

