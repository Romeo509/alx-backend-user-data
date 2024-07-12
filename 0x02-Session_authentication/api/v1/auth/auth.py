#!/usr/bin/env python3
""" Authentication Module
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Manages API authentication """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Validate if a specific path requires authentication """
        if not path or not excluded_paths:
            return True

        if path[-1] != '/':
            path += '/'

        for exc_path in excluded_paths:
            if exc_path.endswith('*'):
                if path.startswith(exc_path[:-1]):
                    return False
            elif path == exc_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Get the Authorization header from the request """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return the current user (None by default) """
        return None

    def session_cookie(self, request=None):
        """ Retrieve the value of the session cookie """
        if request is None:
            return None

        session_name = getenv("SESSION_NAME")
        if not session_name:
            return None

        return request.cookies.get(session_name)
