from aiogram.fsm.state import State, StatesGroup

class Broadcast(StatesGroup):
    cast_text = State()
    cast_image = State()
    cast_doc = State()