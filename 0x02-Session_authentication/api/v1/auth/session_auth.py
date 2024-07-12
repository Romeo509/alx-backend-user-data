#!/usr/bin/env python3
""" Session Authentication Module
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """Handles user sessions for authentication."""
    sessions = {}

    def create_session(self, user_id: str = None) -> str:
        """Generate a new session ID for the given user ID."""
        if not user_id or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.sessions[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Fetch user ID associated with a given session ID."""
        if not session_id or not isinstance(session_id, str):
            return None

        return self.sessions.get(session_id)

    def current_user(self, request=None):
        """Retrieve the current user based on session cookie."""
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        """Log out the user by deleting their session."""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        self.sessions.pop(session_id, None)
        return True
