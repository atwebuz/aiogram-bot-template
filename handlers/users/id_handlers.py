from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp

SUPERUSERS = [1313003485,443322]
BLOCKUSERS = [1330034852,29987271]

@dp.message_handler(chat_id=SUPERUSERS, commands='start') 
async def id_filter_example(message: types.Message): 
    await message.answer('xush kelibsiz, Superuser')

@dp.message_handler(chat_id=BLOCKUSERS, commands='start') 
async def id_filter_example(message: types.Message): 
    await message.answer('siz blockdasiz')
