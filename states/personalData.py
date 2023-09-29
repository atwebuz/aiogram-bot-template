from aiogram.dispatcher.filters.state import StatesGroup, State

class PesonalData(StatesGroup):
    myname = State()
    myemail = State()
    myphone = State()