#!/usr/bin/env python3
"""
    Authentication File Module to handle all DB sessions
"""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the input password """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


class Auth:
    """
        Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
            Initializer(constructor) method
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
            Auth.register_user should take mandatory email and password
            string arguments and return a User object.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hash_pwd = _hash_password(password)
            user = self._db.add_user(email, hash_pwd)

            return user

        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """
            In this task, you will implement the Auth.valid_login method.
            It should expect email and password required arguments and
            return a boolean.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        user_pwd = user.hashed_password
        encoded_pwd = password.encode()

        if bcrypt.checkpw(encoded_pwd, user_pwd):
            return True

        return False
