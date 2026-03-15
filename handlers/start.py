from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from services.user_service import get_user
from keyboards.start import main_kb, register_kb
router = Router()

@router.message(CommandStart())
async def handle_start(
    message: Message,
    ):

    dev_id = "5381044581"
    user_id = str(message.from_user.id)

    if user_id == dev_id:
        await message.answer(
            "Choose your role",
            reply_markup=main_kb
            )
    elif not get_user(user_id):
        await message.answer(
            "Welcome Fren!"
            "\nIn order to use, register first",
            reply_markup=register_kb
            )
    else: 
        await message.answer(
            "Choose your role",
            reply_markup=main_kb
            )