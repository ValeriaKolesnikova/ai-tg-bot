from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext

from keyboards import main_kb as kb
from states.state import ChatState
from ai.generators import generate_text

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text='Hello! This AI bot', reply_markup=kb.main)


@router.message(F.text=='Чат')
async def chat(message: Message, state: FSMContext):
    await state.set_state(ChatState.text)
    await message.answer(text='Введите ваш запрос ChatGPT:')


@router.message(ChatState.text)
async def chat_response(message: Message, state: FSMContext):
    await state.set_state(ChatState.wait)
    response = await generate_text(message.text, 'gpt-3.5-turbo')
    await message.answer(response)
    await state.clear()


@router.message(ChatState.wait)
async def wait_for_response(message: Message):
    await message.answer('Ваш запрос генерируется, подождите')
