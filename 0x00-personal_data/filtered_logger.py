#!/usr/bin/env python3
"""
    function called filter_datum that returns the log message obfuscated:
"""

import re


def filter_datum(fields, redaction, message, separator):
    """
        function called filter_datum that returns the log message
        obfuscated:
    """
    return re.sub(r'('
                  + '|'.join(fields) + r')=[^{}]*'.format(separator),
                  r'\1=' + redaction, message)
