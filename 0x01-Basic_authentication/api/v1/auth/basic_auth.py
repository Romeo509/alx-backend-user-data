#!/usr/bin/env python3
"""
BasicAuth module for handling basic authentication
"""

import base64
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth class for handling basic authentication """

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Extracts the Base64 part of the Authorization
        header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """
        Decodes the Base64 part of the Authorization header
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts user email and password from the Base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        last_colon_index = decoded_base64_authorization_header.rfind(':')
        email = decoded_base64_authorization_header[:last_colon_index]
        password = decoded_base64_authorization_header[last_colon_index + 1:]

        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """
        Returns the User instance based on email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            user = User.search({'email': user_email})
            if not user:
                return None
            user = user[0]
            if not user.is_valid_password(user_pwd):
                return None
            return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the User instance for a request using Basic Authentication
        """
        if request is None:
            return None

        auth_header = self.authorization_header(request)
        base64_auth_header = (
            self.extract_base64_authorization_header(auth_header)
        )
        decoded_auth_header = (
            self.decode_base64_authorization_header(base64_auth_header)
        )
        user_email, user_pwd = (
            self.extract_user_credentials(decoded_auth_header)
        )

        return self.user_object_from_credentials(user_email, user_pwd)
