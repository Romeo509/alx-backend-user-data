#!/usr/bin/env python3
""" Module of Session in Database
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """Session in database Class"""

    def create_session(self, user_id=None):
        """Create a session and store it in the database"""
        session_id = super().create_session(user_id)

        if session_id is None:
            return None

        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        UserSession.save_to_file()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Retrieve a user ID based on a session ID"""
        if session_id is None:
            return None

        UserSession.load_from_file()
        sessions = UserSession.search({'session_id': session_id})

        if not sessions:
            return None

        user_session = sessions[0]
        if user_session.created_at + timedelta(
            seconds=self.session_duration
        ) < datetime.utcnow():
            return None

        return user_session.user_id

    def destroy_session(self, request=None):
        """Destroy a session based on the session ID from the request cookie"""
        if request is None:
            return False

        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        UserSession.load_from_file()
        sessions = UserSession.search({'session_id': session_id})

        if not sessions:
            return False

        user_session = sessions[0]
        user_session.remove()
        UserSession.save_to_file()

        return True
