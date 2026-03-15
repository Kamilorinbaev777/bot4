from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.admin import broadcast_choice
router = Router()

@router.callback_query(F.data == 'admin_role')
async def handle_user_role(
    callback: CallbackQuery
    ):
    await callback.message.edit_text(
        "Your role now an admin!",
        reply_markup=broadcast_choice
        )

    await callback.answer()