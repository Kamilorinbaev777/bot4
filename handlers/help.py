from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command

from keyboards.start import main_kb, back_kb
router = Router()

@router.message(Command('help'))
async def handle_help(
    message: Message
    ):
    await message.answer(
        "The bot is designed to choose a role"
        "\nIncluding basic User, Admin, and Dev",
        reply_markup=back_kb
        )

@router.callback_query(F.data == 'back_from_help')
async def handle_back_btn(
    callback: CallbackQuery
    ):
    await callback.message.answer(
        "Fren!"
        "\nChoose your role from below",
        reply_markup=main_kb
        )
    await callback.answer()