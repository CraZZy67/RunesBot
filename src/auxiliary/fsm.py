from aiogram.fsm.state import StatesGroup, State


class UserInfo(StatesGroup):
    name = State()
    date = State()