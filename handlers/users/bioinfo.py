import logging
from aiogram.dispatcher.filters import Command

from aiogram.types import Message, CallbackQuery
from keyboards.inline.button_menu import categoryMenu, networks_menu ,rezume_menu, bio_menu, download
from aiogram.types import InputFile
from loader import dp

from data.config import ADMINS

@dp.callback_query_handler(text="cancel")
async def canncel_select(call: CallbackQuery):
    faylphoto = InputFile(path_or_bytesio="handlers/Photos/ozim_rasm.jpg")
    await call.message.delete()
    await call.message.answer_photo(photo=faylphoto,caption="<b>Saparkulov Umid</b> backend dasturchisi\n O'zbekiston Respublikasi Toshkent viloyati, Chinoz tumanida tug'ilgan.",reply_markup=categoryMenu)

@dp.callback_query_handler(text="bio")   
async def select_photo(call: CallbackQuery):
    # callback_data = call.data 
    # logging.info(f"{callback_data=}")
    # logging.info(f"{call.from_user.username=}")
   
     # Rasm faylini to'g'ri yo'l bilan yuklash
    # photo_url = "https://miro.medium.com/v2/resize:fit:2400/1*BdiJH7vdd7QSlASW6iVViw.png"
    photo_file = InputFile(path_or_bytesio="handlers/Photos/ozim_rasm.jpg")
    # Xabar matnini tayyorlash
    msg = "<b>Ismi-sharifi:</b>\n"
    msg += "Saparkulov Umidbek Olim o'g'li\n\n"
    msg += "<b>Tug'ilgan yili va joyi:</b>\n"
    msg += "13-avgust 2004-yil;\nToshkent viloyati, Chinoz tumani.\n\n"
    msg += "<b>Ta'limi:</b>\nToshkent davlat texnika universiteti qoshidagi I. Karimov nomidagi akademik lidsey (2020-2022 yillar)\n Toshkent davlat texnika universiteti elektronika avtomatika fakulteti\n <b>yo'nalisi:</b>intellektual muhandislik tizximlari (tarmoqlar va sohalar bo'yicha) 3-kurs talabasiman.\nTramplin IT akademiyasida Backend bo'yicha o'qiyapman.\n"
    msg += "<b>Bilimlar:</b>\n"
    msg += "Python, Django, Django Rest, SQLite, MySQL, PostgreSQL, \nGit, GitHub, HTML, CSS,Telegram Bot, Microsoft Office\n(Word, Excel, Power Point, Paint, va h.k.lar)\n\n"
    msg += "<b>Tillar</b>: o'zbek tili"
    await call.message.delete()
    await call.message.bot.send_photo(chat_id=call.from_user.id, photo=photo_file, caption=msg, reply_markup=bio_menu)
    

@dp.callback_query_handler(text='rezyume')
async def select_category(call: CallbackQuery):
    await call.message.answer(f"Bo'limni tanglang", reply_markup=rezume_menu)
    await call.message.delete()

@dp.callback_query_handler(text='rezume')
async def select_category(call: CallbackQuery):
    with open('handlers/download/rezumefile.pdf', 'rb') as pdf_file:
       await call.message.answer_document(pdf_file, caption="Bu Otajon Bozrboyevni rezumesi", reply_markup=download)
    await call.message.delete()
    

@dp.callback_query_handler(text="networks")
async def buying_course(call: CallbackQuery):
    photonetwork_file = InputFile(path_or_bytesio="handlers/networksphoto/mobil ilovalar.jpg")
    await call.message.answer_photo(photo=photonetwork_file,reply_markup=networks_menu)
    await call.message.delete()

    