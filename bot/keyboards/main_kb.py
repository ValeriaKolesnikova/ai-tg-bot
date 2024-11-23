from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Чат')],
    [KeyboardButton(text='Генерация картинки')]
], resize_keyboard=True, input_field_placeholder='Выберете пункт меню...')


cancel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Отмена')]
])