import asyncio
import threading

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database import connect_db, create_tables

from webserver import run_web

from handlers.start import router as start_router
from handlers.menu import router as menu_router
from handlers.upload import router as upload_router
from handlers.admin import router as admin_router

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(menu_router)
dp.include_router(upload_router)
dp.include_router(admin_router)


async def main():

    await connect_db()
    await create_tables()

    print("BOT STARTED")

    await dp.start_polling(bot)


if __name__ == "__main__":

    threading.Thread(target=run_web).start()

    asyncio.run(main())
