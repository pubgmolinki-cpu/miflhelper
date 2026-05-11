from aiogram import Router, F
from aiogram.types import CallbackQuery, Message

from keyboards import leagues_keyboard, tours_keyboard
from database import get_matches

router = Router()


@router.message(F.text == "⚽ Матчи")
async def show_leagues(message: Message):

    await message.answer(
        "Выберите лигу 👇",
        reply_markup=leagues_keyboard()
    )


@router.callback_query(F.data.startswith("league_"))
async def league_handler(callback: CallbackQuery):

    league = callback.data.split("_")[1]

    await callback.message.edit_text(
        "Выберите тур 👇",
        reply_markup=tours_keyboard(league)
    )


@router.callback_query(F.data.startswith("tour_"))
async def tour_handler(callback: CallbackQuery):

    parts = callback.data.split("_")

    league = parts[1]
    tour = int(parts[2])

    matches = await get_matches(league, tour)

    if not matches:

        await callback.message.answer("⚠️ Тур ещё не заполнен!")
        return

    text = f"🏆 {league} | Тур {tour}\n\n"

    for m in matches:

        text += (
            f"{m['home_team']} {m['home_score']}:{m['away_score']} {m['away_team']}\n"
        )

    await callback.message.answer(text)
