from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.pythonKeyboard import menuPython
from keyboards.default.lang import menuLang
from keyboards.default.taskKeyboard import menuAuth
from states.personalData import PesonalData


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


@dp.message_handler(Command("task"))
async def show_menu(message: Message):
    await message.answer("Tilni tanlang o'ting", reply_markup=menuLang)

@dp.message_handler(text="UZB")

async def show_menu(message: Message):
    await message.answer(f"Uzbek tilini tanladingiz\nIltimos {message.from_user.full_name} royxatdan oring", reply_markup=ReplyKeyboardRemove)

@dp.message_handler(text="ENG")
async def show_menu(message: Message):
    await message.answer(f"You have submitted English\Pleace {message.from_user.full_name} log in", reply_markup=ReplyKeyboardRemove)


# menuTask