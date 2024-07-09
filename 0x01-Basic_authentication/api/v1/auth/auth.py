#!/usr/bin/env python3
from typing import List
from flask import request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if authentication is required for a given path """
        if path is None:
            return True

        if not excluded_paths:
            return True

        # Normalize path by removing trailing slash
        normalized_path = path.rstrip('/')

        for ex_path in excluded_paths:
            normalized_ex_path = ex_path.rstrip('/')
            if normalized_path == normalized_ex_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Placeholder for authorization header handling """
        return None

    def current_user(self, request=None):
        """ Placeholder for current user handling """
        return None
