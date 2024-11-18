import asyncio
import os
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from handlers.user import router as user_router
from handlers.admin import router as admin_router


async def main():
    load_dotenv()

    bot = Bot(token=os.getenv('BOT_TOKEN'))
    dp = Dispatcher()
    dp.include_routers(user_router, admin_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())