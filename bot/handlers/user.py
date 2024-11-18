from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

from keyboards import main_kb as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello! This AI bot', reply_markup=kb.main)

@router.message(F.text=='Чат')
async def chat(message: Message):
    await message.answer('')
