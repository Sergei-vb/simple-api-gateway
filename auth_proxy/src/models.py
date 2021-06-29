from sqlalchemy import Column, Integer, String

from .db import Base


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    username = Column(String(length=256), nullable=False, unique=True)
    email = Column(String(length=128), nullable=False, unique=True)
    first_name = Column(String(length=64), nullable=False)
    last_name = Column(String(length=64), nullable=False)

    def __repr__(self):
        return f'Profile(id={self.id!r}, username={self.username!r})'
