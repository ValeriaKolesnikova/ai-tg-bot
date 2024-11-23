from aiogram.fsm.state import StatesGroup, State


class ChatState(StatesGroup):
    text = State()
    wait = State()


class ImageState(StatesGroup):
    image = State()
    wait = State()