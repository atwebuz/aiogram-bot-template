from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Python'),
            KeyboardButton(text='Js'),
        ],

    ],
    resize_keyboard=True
)