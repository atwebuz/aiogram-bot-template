from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.personalData import PesonalData


from loader import dp


@dp.message_handler(CommandHelp(), state=PesonalData.myname)
async def bot_help(message: types.Message):
    text = ("ismingizni qaytadan kiriting iltimos!")
    
    await message.answer(text)


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))
