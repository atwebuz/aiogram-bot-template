from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuAuth = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Register'),
            KeyboardButton(text='Login'),
        ],
    ],
    resize_keyboard=True
)