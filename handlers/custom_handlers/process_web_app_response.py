from aiogram.fsm.context import FSMContext
from loader import dp
from aiogram import types, F
from database.db import async_session
from database.models import History, Characters
from sqlalchemy import select
from states.states_for_bot import RequestState
from utils.amplitude import post_amplitude_info


@dp.message(F.web_app_data)
async def process_web_app_response(message: types.Message, state: FSMContext):
    await post_amplitude_info(message.from_user.id, "Selected a character")

    async with async_session() as session:
        result = await session.execute(select(History).where(History.user_id == message.from_user.id))
        user_history = result.scalars().first()

        if not user_history:
            new_history = History(user_id=message.from_user.id, character=int(message.web_app_data.data))

            session.add(new_history)
            await session.commit()
        else:
            user_history.character = int(message.web_app_data.data)
            await session.commit()

        result = await session.execute(select(Characters).where(Characters.id == int(message.web_app_data.data)))
        character = result.scalars().first()

        await state.set_state(RequestState.wait_request)
        await message.answer(character.hello_message)
