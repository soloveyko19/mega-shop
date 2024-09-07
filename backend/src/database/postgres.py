from typing import Iterable
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, ForeignKey, String, DECIMAL, Integer, select

import conf


POSTRGES_URL = f"postgresql+asyncpg://{conf.POSTGRES_USERNAME}:{conf.POSTGRES_PASSWORD}@{conf.POSTGRES_HOSTNAME}/{conf.POSTGRES_DB_NAME}"
engine = create_async_engine(url=POSTRGES_URL)
async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
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
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)
    category = relationship("Category", lazy="joined")

    async def save(self) -> None:
        async with async_session() as session:
            session.add(self)
            await session.commit()


    @classmethod
    async def all(cls) -> Iterable['Product']:
        async with async_session() as session:
            query = select(Product).order_by('id')
            res = await session.execute(query)
            return res.scalars().all()
        

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)




