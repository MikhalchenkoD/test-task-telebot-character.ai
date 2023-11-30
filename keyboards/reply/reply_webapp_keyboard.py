from aiogram.types import WebAppInfo
from aiogram import types


def gen_webapp_keyboard():
    web_app = WebAppInfo(url='https://mikhalchenkod.github.io/test-task-telebot-webapp.github.io/')

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='Выбрать персонажа', web_app=web_app)]
        ],
        resize_keyboard=True
    )

    return keyboard