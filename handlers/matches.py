from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import (
    leagues_keyboard,
    tours_keyboard
)

from database import get_matches

router = Router()

@router.callback_query(F.data == "matches")
async def matches_menu(callback: CallbackQuery):

    await callback.message.edit_text(
        "Выберите лигу 👇",
        reply_markup=leagues_keyboard()
    )

@router.callback_query(F.data.startswith("league_"))
async def tours(callback: CallbackQuery):

    league = callback.data.split("_")[1]

    await callback.message.edit_text(
        "Выберите тур 👇",
        reply_markup=tours_keyboard(league)
    )

@router.callback_query(F.data.startswith("tour_"))
async def show_tour(callback: CallbackQuery):

    data = callback.data.split("_")

    league = data[1]
    tour = int(data[2])

    matches = await get_matches(
        league,
        tour
    )

    if not matches:

        await callback.message.answer(
            "⚠️ Тур пока пуст!"
        )

        return

    text = f"🏆 Тур {tour}\n\n"

    for match in matches:

        text += (
            f"{match['home_team']} "
            f"{match['home_score']}:{match['away_score']} "
            f"{match['away_team']}\n\n"
        )

    await callback.message.answer(text)
