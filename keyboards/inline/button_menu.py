from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
# 1- usul:
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🧾  Bio", callback_data="bio"),
            InlineKeyboardButton(text="📂  Rezume", callback_data="rezyume"),
            InlineKeyboardButton(text="📌  Social networks", callback_data="networks")
        ]
           
     ]
)
bio_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="↩️ Ortga", callback_data='cancel')
    ]
])


rezume_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📜 rezyume", callback_data="rezume"),
        InlineKeyboardButton(text="↩️ Ortga", callback_data="cancel")
    ]
])
download = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="↩️ Ortga", callback_data='cancel')
    ]
])




networks_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
      InlineKeyboardButton(text="💼  Git Hub",url="https://github.com/UmidbekSaparkulov",callback_data="git-hub"),
      InlineKeyboardButton(text="🔗  Linked in",url="https://www.linkedin.com/in/umidjon-saparkulov-182a54328/",callback_data="linkedin"),
      InlineKeyboardButton(text="📈  Leetcode",url="https://leetcode.com/u/ZFRBxmd3a6/",callback_data='leetcode'),
    ],
    [
        InlineKeyboardButton(text="✈️  Telegram Akkauntim",url="https://t.me/Umid04013", callback_data='telegram'),
    ],
    [
        InlineKeyboardButton(text="↩️ Ortga", callback_data="cancel")
    ]
])





