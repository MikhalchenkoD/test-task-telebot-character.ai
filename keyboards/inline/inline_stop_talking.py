from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_inline_stop_button():
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Закончить разговор",
        callback_data="cancel",)
    )

    return builder