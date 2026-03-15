import asyncio
import os
from aiogram import Bot, Dispatcher, BaseMiddleware
from aiogram.types import CallbackQuery, Message
from dotenv import load_dotenv

from middlewares.user import userMiddleware

from handlers.start import router as start_router
from handlers.register import router as reg_router
from handlers.help import router as help_router
from handlers.users import router as users_router
from handlers.feedback import router as f_router
from handlers.admin.admin_start import router as admins_router
from handlers.admin.dev_start import router as dev_router
from handlers.admin.broadcast import router as broadcast_router
from handlers.admin.userlist import router as userlist_router

load_dotenv()
TOKEN=os.getenv('TOKEN')
bot = Bot(TOKEN)

async def main():
    
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(reg_router)
    dp.include_router(help_router)
    dp.include_router(users_router)
    dp.include_router(admins_router)
    dp.include_router(dev_router)
    dp.include_router(broadcast_router)
    dp.include_router(userlist_router)
    dp.include_router(f_router)

    #dp.message.middleware(registerMiddleware())
    dp.callback_query.middleware(userMiddleware())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
