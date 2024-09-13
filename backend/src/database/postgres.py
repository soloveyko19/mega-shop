from typing import Iterable, Self
from datetime import datetime as dt

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, DateTime, ForeignKey, String, DECIMAL, Integer, select, exists

import conf
from utils.exceptions import UsernameAlreadyTakenError


POSTRGES_URL = f"postgresql+asyncpg://{conf.POSTGRES_USERNAME}:{conf.POSTGRES_PASSWORD}@{conf.POSTGRES_HOSTNAME}/{conf.POSTGRES_DB_NAME}"
engine = create_async_engine(url=POSTRGES_URL)
async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

class Base(DeclarativeBase):
    pass


class BaseModel:
    id: Column

    @classmethod
    async def all(cls) -> Iterable[Self]:
        async with async_session() as session:
            query = select(cls).order_by('id')
            res = await session.execute(query)
            return res.scalars().unique().all()
    
    @classmethod
    async def get(cls, id_: int) -> Self | None:
        async with async_session() as session:
            query = select(cls).filter(cls.id == id_)
            res = await session.execute(query)
            return res.unique().scalar_one_or_none()


    async def save(self) -> None:
        async with async_session() as session:
            session.add(self)
            await session.commit()


class Product(Base, BaseModel):
    __tablename__ = "products"

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    description = Column(String(4000), nullable=False)
    price = Column(DECIMAL(15, 2), nullable=False)
    image_url = Column(String(2048))

    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    category = relationship("Category", back_populates="products", lazy="joined")

        

class Category(Base, BaseModel):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    products = relationship("Product", back_populates="category", lazy="joined")


class User(Base, BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(255), nullable=False) 
    created_at = Column(DateTime, default=dt.now(), nullable=False)

    @classmethod
    async def check_username_available(cls, username: str) -> bool:
        async with async_session() as session:
            query = select(exists(cls)).filter(cls.username == username)
            res = await session.execute(query)
            if res.scalar_one_or_none():
                raise UsernameAlreadyTakenError("Username already taken")
            return True
    
    @classmethod
    async def get_by_username(cls, username: str) -> Self | None:
        async with async_session() as session:
            query = select(cls).filter(cls.username == username)
            res = await session.execute(query)
            return res.scalar_one_or_none()
