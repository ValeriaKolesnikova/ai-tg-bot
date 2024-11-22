import asyncio
import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from handlers.user import router as user_router
from handlers.admin import router as admin_router
from database.models import async_main


async def main():
    load_dotenv()

    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_routers(user_router, admin_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


async def on_startup(dispatcher):
    await async_main()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())