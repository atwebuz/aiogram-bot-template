from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Kirish'),
            KeyboardButton(text='Batafsil'),
        ],
        [
            KeyboardButton(text='Ortga'),
            KeyboardButton(text='Boshiga'),
        ],
    ],
    resize_keyboard=True
)