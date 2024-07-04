#!/usr/bin/env python3
"""
This module provides a function to obfuscate sensitive data
in log messages by replacing specified field values with a
redaction string.
"""

import re
from typing import List


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
