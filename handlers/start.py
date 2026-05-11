from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards import main_menu

router = Router()

@router.message(Command("start"))
async def start(message: Message):

    text = (
        "🔥 <b>Добро пожаловать в MIFL HELPER!</b>\n\n"
        "Здесь ты можешь:\n"
        "• смотреть матчи\n"
        "• смотреть таблицу\n"
        "• смотреть статистику\n\n"
        "Приятного использования 🔥"
    )

    await message.answer(
        text,
        reply_markup=main_menu()
    )
