#!/usr/bin/env python3
"""
This module provides functions to interact with a MySQL database
using environment variables for secure credentials, obfuscating sensitive data in logs,
and configuring a logger.
"""

import logging
import mysql.connector
import os
import re
from typing import List, Tuple


PII_FIELDS: Tuple[str, ...] = ("name", "email", "password", "ssn", "phone")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
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
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


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
        record.msg = filter_datum(self.fields, self.REDACTION, super().format(record), self.SEPARATOR)
        return super().format(record)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to the MySQL database using environment variables for credentials.

    Returns:
        mysql.connector.connection.MySQLConnection: The database connector object.
    """
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    # Connect to the database
    db = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=db_name
    )

    return db


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


if __name__ == "__main__":
    # Example usage
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM users;")
    for row in cursor:
        print(row[0])
    cursor.close()
    db.close()
