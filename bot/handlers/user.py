from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello! This AI bot')
