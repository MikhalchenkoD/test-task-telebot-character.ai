import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from config_data import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot=bot)