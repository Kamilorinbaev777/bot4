import os
from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery

dev_id = 5381044581
admins = {5381044581, 122, 2333} #garbages

class userMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: CallbackQuery, data):

        if event.data == 'dev_role':
            if event.from_user.id != dev_id:
                await event.message.edit_text(
                    "Acces denied!"
                    "\nYou are not a developer"
                    )
                await event.answer()
                return
            return await handler(event, data)

        if event.data == 'admin_role':
            if event.from_user.id not in admins:
                await event.message.edit_text(
                    "Acces denied!"
                    "\nYou are not an admin"
                    )
                await event.answer()
                return
            return await handler(event, data)

        return await handler(event, data)