#!/usr/bin/env python3
"""
    class BasicAuth that inherits from Auth
"""
from api.v1.auth.auth import Auth
from base64 import b64decode, decode


class BasicAuth(Auth):
    """
        class BasicAuth that inherits from Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
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
