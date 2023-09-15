#!/usr/bin/env python3
"""
    Authentication File Module to handle all DB sessions
"""

import bcrypt


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the input password """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed
