import asyncio
from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext

from storage import load_data

from states.admin.broadcast import Broadcast

from keyboards.admin import dev_menu
from keyboards.admin import broadcast_choice

router = Router()

@router.callback_query(F.data == 'dBroadcast')
async def handle_broadcasting(
    callback: CallbackQuery
    ):
    await callback.message.edit_text(
        "what do you want to broadcast today?",
        reply_markup=broadcast_choice
        )

@router.callback_query(F.data == 'dBcast_text')
async def handle_text_bcasting(
    callback: CallbackQuery,
    state: FSMContext
    ):
    
    await state.set_state(Broadcast.cast_text)
    await callback.message.edit_text(
        "Send me your broadcast publication"
        "\nIn text only!"
        )
    await callback.answer()

@router.callback_query(F.data == 'dBcast_img')
async def handle_text_bcasting(
    callback: CallbackQuery,
    state: FSMContext
    ):
    
    await state.set_state(Broadcast.cast_image)
    await callback.message.edit_text(
        "Send me your broadcast publication"
        "\nAn image with captions (optional)"
        )
    await callback.answer()

@router.callback_query(F.data == 'dBcast_doc')
async def handle_text_bcasting(
    callback: CallbackQuery,
    state: FSMContext
    ):
    
    await state.set_state(Broadcast.cast_doc)
    await callback.message.edit_text(
        "Send me your broadcast publication"
        "\nA document with captions (optional)"
        )
    await callback.answer()

@router.message(Broadcast.cast_text)
async def handle_textcasting_state(
    message: Message,
    state: FSMContext,
    bot: Bot
    ):
    try:
        pub = message.text or ""
    except Exception: 
        await message.answer("text only!")
        return

    users = load_data()

    for user_id in users:
        try:
            await bot.send_message(
                user_id,
                f"{pub}"
                )
        except Exception:
            print(f"failed to send message to user with id {user_id}")
    await state.clear()
    await message.answer(
        "Publication broadcasted successfully!"
        )

@router.message(Broadcast.cast_image)
async def handle_textcasting_state(
    message: Message,
    state: FSMContext,
    bot: Bot
    ):
    try:
        img = message.photo[-1].file_id
        pub = message.caption or ""
    except Exception: 
        await message.answer("Failed, try again")
        return

    users = load_data()

    for user_id in users:
        try:
            await bot.send_photo(
                chat_id=user_id,
                photo=img,
                caption=pub
                )
            await asyncio.sleep(0.05)
        except Exception:
            print(f"Failed to send message to user with id {user_id}")
    await state.clear()
    await message.answer(
        "Publication broadcasted successfully!"
        )

@router.message(Broadcast.cast_doc)
async def handle_textcasting_state(
    message: Message,
    state: FSMContext,
    bot: Bot
    ):
    try:
        doc = message.document.file_id
        pub = message.caption or ""
    except Exception: 
        await message.answer("Failed, try again")
        return

    users = load_data()

    for user_id in users:
        try:
            await bot.send_document(
                chat_id=user_id,
                document=doc,
                caption=pub
                )
        except Exception:
            print(f"Failed to send message to user with id {user_id}")
    await state.clear()
    await message.answer(
        "Publication broadcasted successfully!"
        )