from sqlalchemy import select, update
from decimal import Decimal

from .models import User, async_session, AiModel, AiType, Order


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, balance=0))
            await session.commit()


async def get_user(tg_id):
    async with async_session() as session:
       return await session.scalar(select(User).where(User.tg_id == tg_id))


async def calculate(tg_id, summ, model_name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        model = await session.scalar(select(AiModel).where(AiModel.name == model_name))
        updated_balance = Decimal(Decimal(user.balance) - Decimal(Decimal((model.price) * Decimal(summ))))
        await session.execute(update(User).where(User.id == user.id).values(balance=str(updated_balance)))
        await session.commit()