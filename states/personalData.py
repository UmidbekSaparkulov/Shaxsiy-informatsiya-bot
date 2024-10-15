from aiogram.dispatcher.filters.state import StatesGroup, State

class PersonalData(StatesGroup):
    fullname = State()
    email = State()
    born = State()
    study = State()
    millati = State()
    phoneNumber = State()

