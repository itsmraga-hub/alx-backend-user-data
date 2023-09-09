#!/usr/bin/env python3
"""
    Now you will create a class to manage the API authentication.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
        Now you will create a class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            returns False - path and excluded_paths will be used later,
            now, you don’t need to take care of them
        """

        if path is None or excluded_paths is None or not len(excluded_paths):
            return True

        if path[-1] != '/':
            path += '/'

        astericks = [stars[:-1]
                     for stars in excluded_paths if stars[-1] == '*']

        for stars in astericks:
            if path.startswith(stars):
                return False

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
            returns None - request will be the Flask request object
        """
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
            returns None - request will be the Flask request object
        """
        return None

    def session_cookie(self, request=None):
        """
            Returns a cookie value from a request
        """

        if request is None:
            return None

        SESSION_NAME = getenv("SESSION_NAME")

        if SESSION_NAME is None:
            return None

        session_id = request.cookies.get(SESSION_NAME)

        return session_id
