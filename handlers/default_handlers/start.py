from database.db import async_session
from database.models import Users
from aiogram import types
from aiogram.filters import Command
from loader import dp
from keyboards.reply.reply_webapp_keyboard import gen_webapp_keyboard
from utils.amplitude import post_amplitude_info


@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    await post_amplitude_info(message.from_user.id, "Registration")

    async with async_session() as session:
        fullname = message.from_user.full_name.split()
        new_user = Users(user_id=message.from_user.id, username=message.from_user.username,
                        name=fullname[0], surname=fullname[1])

        session.add(new_user)
        await session.commit()

    await message.answer("""
    👋 Добро пожаловать!
    Этот бот позволяет вам общаться с персонажами.

    Важно помнить:

    🤥 Все, что говорят персонажи, вымышлено! Не доверяйте всему, что они говорят, или не воспринимайте слишком серьезно.

    🤬 Персонажи могут случайно произнести оскорбительные слова - пожалуйста, не обижайтесь на них.

    Мы надеемся, что вам будет весело!
    """, reply_markup=gen_webapp_keyboard())

