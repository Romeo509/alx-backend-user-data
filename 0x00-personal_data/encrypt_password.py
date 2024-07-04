#!/usr/bin/env python3
"""
This module provides functions to hash passwords
and validate them using bcrypt.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt and returns the salted, hashed password.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The salted, hashed password.
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against a hashed password using bcrypt.

    Args:
        hashed_password (bytes): The hashed password stored in bytes.
        password (str): The password to validate.

    Returns:
        bool: True if the password matches the hashed
        password, False otherwise.
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
