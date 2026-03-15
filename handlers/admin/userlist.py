from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from storage import load_data, save_data
from states.admin.del_user import User
from keyboards.admin import reject_del, dev_menu
from keyboards.admin import delete_user_kb, back_to_menu
router = Router()

@router.callback_query(F.data == 'dList')
async def get_list_of_users(
    callback: CallbackQuery
    ):
    all_users = load_data()
    await callback.message.edit_text(
        "List of all users"
        f"\n{all_users}",
        reply_markup=delete_user_kb
        )
    await callback.answer()

@router.callback_query(F.data == 'dUser')
async def delete_user(
    callback: CallbackQuery,
    state: FSMContext
    ):
    all_users = load_data()
    await state.set_state(User.user_id)
    await callback.message.edit_text(
        "List of all users"
        f"\n{all_users}"
        "\nSend user id delete"
    )
    await callback.answer()

@router.callback_query(F.data == 'dDel')
async def reject_deletion(
    callback: CallbackQuery,
    state: FSMContext
    ):
    await state.clear()
    await callback.message.edit_text(
        "User deletion process cancelled",
        reply_markup=back_to_menu
        )
    await callback.answer()

@router.callback_query(F.data == 'dBack')
async def back_to_devmenu(
    callback: CallbackQuery
    ):
    await callback.message.edit_text(
        "Hello Developer!",
        reply_markup=dev_menu
        )

@router.message(User.user_id)
async def delete_user_by_id(
    message: Message,
    state: FSMContext,
    bot: Bot
    ):
    user_id = str(message.text)
    all_users = load_data()
    
    if user_id in all_users:
        del all_users[user_id]
        save_data(all_users)
        await message.answer(
            f"user with id: {user_id}"
            " successfully deleted from the bot"
            )
        await bot.send_message(
            user_id, 
            "You are deleted from the bot"
            "\nBy the developer!"
            )
        await state.clear()
    else: 
        await message.answer(
            "Invalid ID, please try again"
            " sending a valid ID",
            reply_markup=reject_del
            )
        return