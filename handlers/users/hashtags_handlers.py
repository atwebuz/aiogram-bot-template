from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp

@dp.message_handler(hashtags='money') ## -> #money
@dp.message_handler(cashtags=['eur','usd']) ## -> $EUR, $USD 
async def hashtag_example(message: types.Message): 
    await message.answer('xashtags')

