from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuLang = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='UZB'),
            KeyboardButton(text='ENG'),
        ],
    ],
    resize_keyboard=True
)