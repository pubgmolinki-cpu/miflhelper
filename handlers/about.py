from aiogram import Router, F
from aiogram.types import CallbackQuery

router = Router()

@router.callback_query(F.data == "about")
async def about(callback: CallbackQuery):

    text = (

        "ℹ️ <b>MIFL HELPER</b>\n\n"

        "Бот для MIFL лиги.\n\n"

        "Функции:\n"
        "• Матчи\n"
        "• Таблица\n"
        "• Статистика\n"
        "• Игроки\n"
        "• MOTM\n\n"

        "Powered by MIFL 🔥"

    )

    await callback.message.answer(text)
