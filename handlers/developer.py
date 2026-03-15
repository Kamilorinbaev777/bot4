from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

#from main import bot
from storage import load_data, save_data
from states.users import User
from keyboards.developer import list_kb, reject_del
from keyboards.developer import delete_user_kb, back_to_menu
router = Router()

@router.callback_query(F.data == 'dev_role')
async def handle_user_role(
    callback: CallbackQuery
    ):
    await callback.message.edit_text(
        "Hello Developer!",
        reply_markup=list_kb
        )

    await callback.answer()

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
        reply_markup=list_kb
        )

@router.message(User.user_id)
async def delete_user_by_id(
    message: Message,
    state: FSMContext
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
        await state.clear()
    else: 
        await message.answer(
            "Invalid ID, please try again"
            " sending a valid ID",
            reply_markup=reject_del
            )
        return