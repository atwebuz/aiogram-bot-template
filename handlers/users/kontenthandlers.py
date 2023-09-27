from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp

@dp.message_handler(content_types='document')
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def photo_handler(message: types.Message): 
    await message.answer('nima bu?')

@dp.message_handler(content_types=types.ContentType.STICKER)
async def photo_handler(message: types.Message): 
    await message.answer('qanqa sticker bu?')

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def photo_handler(message: types.Message): 
    await message.answer('qanqa odam bu?')

@dp.message_handler(content_types=types.ContentType.VOICE)
async def photo_handler(message: types.Message): 
    await message.answer('qanqa ovoz bu?')
