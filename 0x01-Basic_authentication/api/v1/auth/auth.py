#!/usr/bin/env python3
"""
    Now you will create a class to manage the API authentication.
"""

from flask import request


class Auth:
    """
        Now you will create a class to manage the API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        return False

    def authorization_header(self, request=None) -> str:
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        return None
