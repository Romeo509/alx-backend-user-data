#!/usr/bin/env python3
from typing import List
from flask import request


class Auth:
    def authorization_header(self, request=None) -> str:
        """ Returns the Authorization header value from the request """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """ Checks if authentication is required for a given path """
        if path is None:
            return True

        if not excluded_paths:
            return True

        normalized_path = path.rstrip('/')

        for ex_path in excluded_paths:
            normalized_ex_path = ex_path.rstrip('/')
            if normalized_path == normalized_ex_path:
                return False

        return True

    def current_user(self, request=None):
        """ Placeholder for current user handling """
        return None
