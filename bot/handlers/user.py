from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from decimal import Decimal

from keyboards import main_kb as kb
from states.state import ChatState
from ai.generators import generate_text
from database.requests import set_user, get_user, calculate

router = Router()


@router.message(F.text=='Отмена')
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await set_user(message.from_user.id)
    await message.answer(text='Hello! This AI bot', reply_markup=kb.main)
    await state.clear()


@router.message(F.text=='Чат')
async def chat(message: Message, state: FSMContext):
    user = await get_user(message.from_user.id)
    if Decimal(user.balance) > 0:
        await state.set_state(ChatState.text)
        await message.answer(text='Введите ваш запрос ChatGPT:', reply_markup=kb.cancel)
    else:
        await message.answer('Недостаточно средств на балансе')


@router.message(ChatState.text)
async def chat_response(message: Message, state: FSMContext):
    await state.set_state(ChatState.wait)
    response = await generate_text(message.text, 'gpt-3.5-turbo')
    await calculate(message.from_user.id, response['tokens'], 'gpt-4o')
    await message.answer(response['response'])
    await state.set_state(ChatState.text)


@router.message(ChatState.wait)
async def wait_for_response(message: Message):
    await message.answer('Ваш запрос генерируется, подождите')
