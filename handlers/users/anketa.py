from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PesonalData


@dp.message_handler(Command("anketa"))
async def enter_test(message: types.Message):
    await message.answer("Toliq ism kiriting")
    await PesonalData.myname.set()


@dp.message_handler(state=PesonalData.myname)
async def answer_name(message: types.Message, state: FSMContext):
    myname = message.text
    await state.update_data(
        {'name': myname}
    )

    await message.answer("email kiriting")
    await PesonalData.next()


@dp.message_handler(state=PesonalData.myemail)
async def answer_email(message: types.Message, state: FSMContext):
    myemail = message.text
    await state.update_data(
        {'email': myemail}
    )

    await message.answer("phone kiriting")
    await PesonalData.next()

@dp.message_handler(state=PesonalData.myphone)
async def answer_phone(message: types.Message, state: FSMContext):
    myphone = message.text
    await state.update_data(
        {'phone': myphone}
    )

    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    msg = 'malumotla qabul boldi\n'
    msg += f"ismingiz - {name}\n"
    msg += f"email - {email}\n"
    msg += f"phone - {phone}\n"
    await message.answer(msg)

    await state.finish()
    

