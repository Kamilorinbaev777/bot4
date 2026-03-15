from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from states.register import Register
from services.user_service import create_user
from keyboards.start import main_kb
router = Router()

@router.callback_query(F.data == 'register')
async def handle_register(
    callback: CallbackQuery,
    state: FSMContext
    ):
    await state.set_state(Register.name)
    await callback.message.edit_text(
        "What is your name?"
        )
    await callback.answer()

@router.message(Register.name)
async def handle_name_state(
    message: Message,
    state: FSMContext
    ):
    user_id = str(message.from_user.id)
    user_name = message.text
    
    create_user(user_id, user_name)
    await state.clear()
    await message.answer(
        "Your name saved successfully"
        "\nNow choose your role",
        reply_markup=main_kb
        )