import logging
from aiogram.types import InputFile
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline.button_menu import categoryMenu
from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")
    users = {message.from_user.id:message.from_user.username}
    faylphoto = InputFile(path_or_bytesio="handlers/Photos/ozim_rasm.jpg")
    await message.answer_photo(photo=faylphoto, caption=f" 👋🏻 Salom xurmatli foydalanuvchi {message.from_user.username}!\n Admin botimga 🙋‍♂️ xush kelibsiz", reply_markup=categoryMenu)

    



