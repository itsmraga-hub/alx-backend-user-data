#!/usr/bin/env python3
"""
    function called filter_datum that returns the log message obfuscated:
"""

import re
import logging
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        log_message = super().format(record)
        return re.sub(r'(' + '|'.join(self.fields) +
                      r')=[^{}]*'.format(self.SEPARATOR),
                      r'\1=' + self.REDACTION, log_message)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
        function called filter_datum that returns the log message
        obfuscated:
    """
    return re.sub(r'('
                  + '|'.join(fields) + r')=[^{}]*'.format(separator),
                  r'\1=' + redaction, message)
