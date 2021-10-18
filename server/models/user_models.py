import uuid
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, JSON, String, UniqueConstraint
from sqlalchemy.orm import relationship

from .base import Base


class User(Base):
    """ User Model for storing User related details """
    ID_KEY = "id"
    NAME_KEY = "name"
    DATA_KEY = "data"
    EMAIL_KEY = "email"
    PROJECT_ID_KEY = "project_id"

    __tablename__ = "users"

    id = Column(String(32), primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    registered_on = Column(DateTime, default=None)
    data = Column(JSON)

    tokens = relationship('Token', backref='user', cascade="all, delete-orphan", lazy='dynamic')

    def __init__(self, name, email):
        self.id = str(uuid.uuid4().hex)
        self.name = name
        self.email = email
        self.registered_on = datetime.utcnow()

    def to_json(self):
        return {
            self.ID_KEY: self.id,
            self.NAME_KEY: self.name,
            self.EMAIL_KEY: self.email,
            self.DATA_KEY: self.data,
        }


class Token(Base):
    ID_KEY = "id"

    __tablename__ = 'tokens'

    id = Column(String(36), primary_key=True)
    refresh_token = Column(String(255), nullable=False)
    user_id = Column(String(32), ForeignKey('users.id'), nullable=False)

    def __init__(self, token_id, refresh_token, user_id):
        self.id = token_id
        self.refresh_token = refresh_token
        self.user_id = user_id

    def to_json(self):
        return {
            self.ID_KEY: self.id
        }
