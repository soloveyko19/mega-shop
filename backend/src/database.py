from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from conf import POSTGRES_HOSTNAME


POSTRGES_URL = f"postgresql+asyncpg://{POSTGRES_HOSTNAME}/shop"
engine = create_async_engine(url=POSTRGES_URL)
async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()


