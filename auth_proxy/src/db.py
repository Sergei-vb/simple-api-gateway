from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import NullPool

from . import settings


Base = declarative_base()
engine = create_async_engine(settings.DB_DSN, poolclass=NullPool)
session_local = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
