#!/usr/bin/env python3
"""
    Create a class SessionAuth that inherits from Auth
    instance for the variable auth depending of the value of the
    environment variable AUTH_TYPE, If AUTH_TYPE is equal to session_auth:
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """
        Create a class SessionAuth that inherits from Auth
        instance for the variable auth depending of the value of the
        environment variable AUTH_TYPE, If AUTH_TYPE is equal to
        session_auth:
    """
    user_id_by_session_id = {}

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
