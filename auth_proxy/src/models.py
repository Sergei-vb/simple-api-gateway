from sqlalchemy import Column, Integer, JSON, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import PasswordType

from .db import Base


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    username = Column(String(length=256), nullable=False, unique=True)
    email = Column(String(length=128), nullable=False, unique=True)
    first_name = Column(String(length=64), nullable=False)
    last_name = Column(String(length=64), nullable=False)
    password = Column(
        PasswordType(schemes=['pbkdf2_sha512', 'md5_crypt'], deprecated=['md5_crypt']),
        unique=False,
        nullable=False,
    )

    def __repr__(self):
        return f'Profile(id={self.id!r}, username={self.username!r})'


class Session(Base):
    __tablename__ = 'session'

    session_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, unique=True)
    payload = Column(JSON(), nullable=False)
