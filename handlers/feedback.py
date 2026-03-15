from aiogram import Bot, Router, F
from aiogram.types import Message

router = Router()
Fchat_id = -4811395064
dev_id = 5381044581

@router.message(F.sticker)
async def get_sticker(
    message: Message,
    bot: Bot
    ):
    await bot.send_sticker(
        chat_id=Fchat_id,
        sticker=message.sticker
        )
    await bot.send_message(
        chat_id=Fchat_id,
        text=f"\nFrom @{message.from_user.username}"
        )

@router.message(F.photo)
async def get_sticker(
    message: Message,
    bot: Bot
    ):
    if message.from_user.id != dev_id:
        await bot.send_photo(
            chat_id=Fchat_id,
            photo=message.photo[-1].file_id,
            caption=f"{message.caption}"
            f"\nFrom @{message.from_user.username}"
            )

@router.message(F.document)
async def get_sticker(
    message: Message,
    bot: Bot
    ):
    if message.from_user.id != dev_id:
        await bot.send_photo(
            chat_id=Fchat_id,
            photo=message.photo[-1].file_id,
            caption=f"{message.caption}"
            f"\nFrom @{message.from_user.username}"
            )

@router.message()
async def handle_fallback(
    message: Message,
    bot: Bot
    ):
    if message.from_user.id != dev_id:
        await bot.send_photo(
            chat_id=Fchat_id,
            photo=message.photo[-1].file_id,
            caption=f"{message.caption}"
            f"\nFrom @{message.from_user.username}"
            )