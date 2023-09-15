#!/usr/bin/env python3
"""
    Authentication File Module to handle all DB sessions
"""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


def _hash_password(password: str) -> str:
    """ Returns a salted hash of the input password """
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed


def _generate_uuid() -> str:
    """
        the function should return a string representation of a new UUID
    """
    unique_str = uuid.uuid4()
    return str(unique_str)


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

    def create_session(self, email: str) -> str:
        """
            Auth.create_session method. It takes an email string argument
            and returns the session ID as a string.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()

        self._db.update_user(user.id, session_id=session_id)

        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """
            Auth.get_user_from_session_id method. It takes a single
            session_id string argument and returns the corresponding User
            or None.
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        """
            Auth.destroy_session. The method takes a single user_id integer
            argument and returns None.
        """
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        self._db.update_user(user.id, session_id=None)

        return None
