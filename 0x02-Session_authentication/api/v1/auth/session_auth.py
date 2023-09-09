#!/usr/bin/env python3
"""
    Create a class SessionAuth that inherits from Auth
    instance for the variable auth depending of the value of the
    environment variable AUTH_TYPE, If AUTH_TYPE is equal to session_auth:
"""

from api.v1.auth.auth import Auth
from typing import Dict
import uuid


class SessionAuth(Auth):
    """
        Create a class SessionAuth that inherits from Auth
        instance for the variable auth depending of the value of the
        environment variable AUTH_TYPE, If AUTH_TYPE is equal to
        session_auth:
    """
    user_id_by_session_id: Dict[str, str] = {}

    def create_session(self, user_id: str str = None) -> str:
        """
            creates a Session ID for a user_id:
            Return None if user_id is None
            Return None if user_id is not a string
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
            Returns session id based on user id
            Return None if session_id is None
            Return None if session_id is not a string
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id, None)

    def current_user(self, request=None):
        """
            (overload) that returns a User instance based on a cookie value:
        """
        cookie = self.session_cookie(request)
        session_user_id = self.user_id_for_session_id(cookie)
        user_id = User.get(session_user_id)
        return user_id

    def destroy_session(self, request=None):
        """
            that deletes user session / logout(out)
        """
        cookie_data = self.session_cookie(request)
        if cookie_data is None:
            return False
        if not self.user_id_for_session_id(cookie_data):
            return False
        del self.user_id_by_session_id[cookie_data]
        return True
