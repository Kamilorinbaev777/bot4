from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.admin import dev_menu
router = Router()

@router.callback_query(F.data == 'dev_role')
async def handle_user_role(
    callback: CallbackQuery
    ):
    await callback.message.edit_text(
        "Hello Developer!",
        reply_markup=dev_menu
        )
    await callback.answer()