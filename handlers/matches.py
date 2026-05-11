from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import leagues_keyboard, tours_keyboard
from database import get_matches

router = Router()

@router.message(F.text == "⚽ Матчи")
async def matches(message):

    await message.answer(
        "Выберите лигу 👇",
        reply_markup=leagues_keyboard()
    )

@router.callback_query(F.data.startswith("league_"))
async def league(callback: CallbackQuery):

    league = callback.data.split("_")[1]

    await callback.message.edit_text(
        "Выберите тур 👇",
        reply_markup=tours_keyboard(league)
    )

@router.callback_query(F.data.startswith("tour_"))
async def tour(callback: CallbackQuery):

    data = callback.data.split("_")

    league = data[1]
    tour = int(data[2])

    matches = await get_matches(league, tour)

    if not matches:
        await callback.message.answer("⚠️ Тур ещё не заполнен!")
        return

    text = f"🏆 Тур {tour}\n\n"

    for m in matches:

        text += f"{m['home_team']} {m['home_score']}:{m['away_score']} {m['away_team']}\n"

    await callback.message.answer(text)
