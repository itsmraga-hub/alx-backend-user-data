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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Validates the provided password matches the hashed password """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
