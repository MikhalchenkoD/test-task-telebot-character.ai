from aiogram.fsm.context import FSMContext
from loader import dp
from aiogram import types, F


@dp.callback_query(F.data == "cancel")
async def send_random_value(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("Разговор закончен. Выберите нового персонажа")
