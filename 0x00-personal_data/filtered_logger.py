#!/usr/bin/env python3
"""
This module provides a function to obfuscate sensitive data
in log messages by replacing specified field values with a
redaction string, a logging formatter to use it, and a logger
setup to handle log messages.
"""

import re
import logging
from typing import List, Tuple

PII_FIELDS: Tuple[str, ...] = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    Obfuscates the values of specified fields in a log message.

    Args:
        fields (List[str]): A list of strings representing all
            fields to obfuscate.
        redaction (str): A string representing by what the field
            will be obfuscated.
        message (str): A string representing the log line.
        separator (str): A string representing by which character
            is separating all fields in the log line (message).

    Returns:
        str: The log message with specified field values obfuscated.
    """
    pattern = '|'.join([
        f'{field}=[^{separator}]*' for field in fields
    ])
    return re.sub(
        pattern,
        lambda m: m.group().split('=')[0] + '=' + redaction,
        message
    )


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with the specified fields to redact.

        Args:
            fields (List[str]): The fields to redact in the log message.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the specified log record.

        Args:
            record (logging.LogRecord): The log record to format.

        Returns:
            str: The formatted log record with specified fields redacted.
        """
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Creates a logger named "user_data" to log messages with a
    specified formatting and redaction.

    Returns:
        logging.Logger: The configured logger object.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger
