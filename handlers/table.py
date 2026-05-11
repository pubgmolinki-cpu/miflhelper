from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import leagues_keyboard
from database import get_table

router = Router()

@router.callback_query(F.data == "table")
async def table_menu(callback: CallbackQuery):

    await callback.message.edit_text(
        "Выберите лигу 👇",
        reply_markup=leagues_keyboard()
    )

@router.callback_query(F.data.startswith("table_"))
async def show_table(callback: CallbackQuery):

    league = callback.data.split("_")[1]

    clubs = await get_table(league)

    if not clubs:

        await callback.message.answer(
            "⚠️ Таблица пока пустая!"
        )

        return

    text = "📊 <b>Таблица</b>\n\n"

    pos = 1

    for club in clubs:

        text += (

            f"{pos}. {club['name']}\n"
            f"Очки: {club['points']}\n"
            f"Голы: {club['goals_scored']}-"
            f"{club['goals_conceded']}\n\n"

        )

        pos += 1

    await callback.message.answer(text)
