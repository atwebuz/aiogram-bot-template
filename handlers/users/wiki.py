from aiogram import types
from loader import dp
import wikipedia
wikipedia.set_lang('uz')



# Wiki bot
@dp.message_handler(state=None)
async def bot_wiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except TypeError:
        await message.answer("Bu so'rov mavjud emas")
