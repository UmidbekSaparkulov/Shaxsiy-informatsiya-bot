from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), CommandStart())
async def start_b(message: types.Message):
    await message.answer(f"Salom, {from_user.full_name}, siz guruhdasiz!")
    