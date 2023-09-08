#!/usr/bin/env python3
"""
    class BasicAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
from base64 import b64decode, decode
from typing import Tuple, TypeVar
from models.user import User


class BasicAuth(Auth):
    """
        class BasicAuth that inherits from Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header:
                                            str) -> str:
        """
            returns the Base64 part of the Authorization header for a
            Basic Authentication:
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if authorization_header[0:6] == 'Basic ':
            return authorization_header[6:]

        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """
            returns the decoded value of a Base64 string
            base64_authorization_header
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_str = b64decode(base64_authorization_header)
            return decoded_str.decode('utf-8')

        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
            returns the user email and password from the Base64 decoded
            value.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        name_p = decoded_base64_authorization_header.split(':')
        return tuple(name_p)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
            returns the User instance based on his email and password.
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search(email=user_email)
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user

        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
            class BasicAuth that overloads Auth and retrieves the User
            instance for a request:
        """
        auth_header = self.authorization_header(request)
        if not auth_header:
            return None
        extract_base64 = self.extract_base64_authorization_header(auth_header)
        decode_base64 = self.decode_base64_authorization_header(extract_base64)
        user_credentials = self.extract_user_credentials(decode_base64)
        user_email = user_credentials[0]
        user_password = user_credentials[1]
        user_credentials = self.user_object_from_credentials(
            user_email, user_password)
        return user_credentials
