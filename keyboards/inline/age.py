from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ages = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="2-sinf", callback_data='2-sinf'), InlineKeyboardButton(text="3-sinf", callback_data="3-sinf")],
        [InlineKeyboardButton(text="4-sinf", callback_data='4-sinf'), InlineKeyboardButton(text="5-sinf", callback_data="5-sinf")],
        [InlineKeyboardButton(text="6-sinf", callback_data="6-sinf")],
    ]
)


