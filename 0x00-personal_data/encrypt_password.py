#!/usr/bin/env python3
"""
    Implement a hash_password function that expects one string argument
    name password and returns a salted, hashed password, which is a byte
    string.
    Use the bcrypt package to perform the hashing (with hashpw).
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """ Returns a salted, hashed password, which is a byte string """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed

