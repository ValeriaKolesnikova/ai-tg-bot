import os
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import ForeignKey, String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

load_dotenv()

engine = create_async_engine(
    url=os.getenv('DB_URL'),
    echo=True
)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    balance: Mapped[str] = mapped_column(String(length=15))


class AiType(Base):
    __tablename__ = 'ai_types'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=25))


class AiModel(Base):
    __tablename__ = 'ai_models'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(length=25))
    model: Mapped[int] = mapped_column(ForeignKey('ai_types.id'))


class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True)
    status: Mapped[str] = mapped_column(String(length=50))
    order: Mapped[str] = mapped_column(String(length=100))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    amount: Mapped[str] = mapped_column(String(length=15))
    created_at: Mapped[datetime]


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)