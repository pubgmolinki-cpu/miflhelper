import asyncio
import threading

from aiogram import Bot
from aiogram import Dispatcher

from config import BOT_TOKEN

from database import (
    connect_db,
    create_tables
)

from webserver import run_web

from handlers.start import (
    router as start_router
)

from handlers.matches import (
    router as matches_router
)

from handlers.table import (
    router as table_router
)

from handlers.about import (
    router as about_router
)

from handlers.admin import (
    router as admin_router
)

from handlers.stats import (
    router as stats_router
)

from handlers.back import (
    router as back_router
)

bot = Bot(BOT_TOKEN)

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(matches_router)
dp.include_router(table_router)
dp.include_router(about_router)
dp.include_router(admin_router)
dp.include_router(stats_router)
dp.include_router(back_router)

async def main():

    await connect_db()

    await create_tables()

    print("MIFL HELPER STARTED")

    await dp.start_polling(bot)

if __name__ == "__main__":

    threading.Thread(
        target=run_web
    ).start()

    asyncio.run(main())
