from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.pythonKeyboard import menuPython

from loader import dp

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Kurslarni tanlang", reply_markup=menu)

@dp.message_handler(text="Js")
async def show_menu(message: Message):
    await message.answer(f"siz js mavzu tanladingiz: https://t.me/abdusattorov_dev" )

@dp.message_handler(text="Python")
async def show_menu(message: Message):
    await message.answer("Mavzu tanlang", reply_markup=menuPython)

@dp.message_handler(text="Batafsil")
async def show_menu(message: Message):
    await message.answer("Batafsil tanladingiz", reply_markup=ReplyKeyboardRemove())