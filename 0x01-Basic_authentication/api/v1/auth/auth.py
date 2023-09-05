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

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        """
            returns None - request will be the Flask request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            returns None - request will be the Flask request object
        """
        return None
