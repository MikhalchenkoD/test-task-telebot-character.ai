from aiogram.fsm.state import StatesGroup, State


class RequestState(StatesGroup):
    wait_request = State()