from aiogram.fsm.state import State, StatesGroup

class User(StatesGroup):
    user_id = State()