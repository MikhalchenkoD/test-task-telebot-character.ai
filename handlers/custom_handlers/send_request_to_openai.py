import json
import aiohttp
from aiogram.types import Message
from loader import dp
from database.db import async_session
from database.models import History, Characters
from sqlalchemy import select
from states.states_for_bot import RequestState
from utils.amplitude import post_amplitude_info
from utils.request_to_openai import request_to_openai
from keyboards.inline.inline_stop_talking import get_inline_stop_button


@dp.message(RequestState.wait_request)
async def get_response_from_openai(message: Message):
    await post_amplitude_info(message.from_user.id, 'User post request')

    async with async_session() as session:
        result = await session.execute(select(History).where(History.user_id == message.from_user.id))
        user_history = result.scalars().first()

        character_desc_for_openai = {
            1: 'Играй роль как будто ты настояший Марио из компьютерной игры',
            2: 'Играй роль как будто ты настояший Альберт Энштейн, физик теоретик'
        }

        result = request_to_openai(message.text, character_desc_for_openai[user_history.character])

        await post_amplitude_info(message.from_user.id, 'Get an answer')
        await message.answer(result,
                             reply_markup=get_inline_stop_button().as_markup())
        await post_amplitude_info(message.from_user.id, 'Sent a reply')



        # messages = [
        #     {"role": "system", "content": character_desc_for_openai[user_history.character]},
        #     {"role": "user", "content": f"{message.text}"}
        # ]
        # endpoint = 'http://95.217.14.178:8080/candidates_openai/gpt'
        # headers = {
        #     'accept': 'application/json',
        #     'Content-Type': 'application/json'
        # }
        # data = {
        #     'model': 'gpt-3.5-turbo',
        #     'messages': messages,
        # }
        # data = json.dumps(data)
        # async with aiohttp.ClientSession() as session:
        #     async with session.post(endpoint, headers=headers, data=data) as response:
        #         result = await response.json()