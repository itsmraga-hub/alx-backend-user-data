#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from typing import TypeVar

from user import Base, User


class DB:
    """DB class for Object Relational Mapping
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
            Implement the add_user method, which has two required string
            arguments: email and hashed_password, and returns a User object
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """
             implement the DB.find_user_by method
        """
        if not kwargs:
            raise InvalidRequestError

        columns = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in columns:
                raise InvalidRequestError

        user = self._session.query(User).filter_by(**kwargs).first()

        if user is None:
            raise NoResultFound

        return user

    def update_user(self, user_id: int, **kwargs) -> None:
        """
            In this task, you will implement the DB.update_user method that
            takes as argument a required user_id integer and arbitrary
            keyword arguments, and returns None.
        """
        user = self.find_user_by(id=user_id)
        columns = User.__table__.columns.keys()
        for key in kwargs.keys():
            if key not in columns:
                raise ValueError

        for key, value in kwargs.items():
            setattr(user, key, value)

        self._session.commit()
