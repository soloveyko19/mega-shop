from typing import Iterable
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, String, DECIMAL, Integer, select

import conf


POSTRGES_URL = f"postgresql+asyncpg://{conf.POSTGRES_USERNAME}:{conf.POSTGRES_PASSWORD}@{conf.POSTGRES_HOSTNAME}/{conf.POSTGRES_DB_NAME}"
engine = create_async_engine(url=POSTRGES_URL)
async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(4000), nullable=False)
    price = Column(DECIMAL(15, 2), nullable=False)
    image_url = Column(String(2048))

    async def save(self) -> 'Product':
        async with async_session() as session:
            session: AsyncSession
            session.add(self)
            await session.commit()

    @classmethod
    async def all(cls) -> Iterable['Product']:
        async with async_session() as session:
            session: AsyncSession
            query = select(Product).order_by('id')
            res = await session.execute(query)
            return res.scalars().all()
