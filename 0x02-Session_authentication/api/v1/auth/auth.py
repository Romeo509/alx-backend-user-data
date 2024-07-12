#!/usr/bin/env python3
"""
Module for handling API authentication
"""
from typing import List
from flask import request


class Auth:
    """
    Class for managing API authentication
    """

    def authorization_header(self, request=None) -> str:
        """
        Returns the Authorization header value from the request

        Args:
            request (flask.Request): The Flask request object

        Returns:
            str: The value of the Authorization header, or None if not present
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Checks if authentication is required for a given path

        Args:
            path (str): The path to check
            excluded_paths (List[str]): A list of paths that
            do not require authentication

        Returns:
            bool: True if authentication is required, False otherwise
        """
        if path is None:
            return True

        if not excluded_paths:
            return True

        normalized_path = path.rstrip('/')

        for ex_path in excluded_paths:
            normalized_ex_path = ex_path.rstrip('/')
            if '*' in normalized_ex_path:
                # If ex_path ends with '*', match the prefix
                prefix = normalized_ex_path.rstrip('*')
                if normalized_path.startswith(prefix):
                    return False
            elif normalized_path == normalized_ex_path:
                return False

        return True

    def current_user(self, request=None):
        """
        Placeholder for current user handling

        Args:
            request (flask.Request): The Flask request object

        Returns:
            None: Placeholder return value
        """
        return None
