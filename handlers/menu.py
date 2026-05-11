from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards import leagues_keyboard, tours_keyboard
from database import get_matches

router = Router()


# =========================
# МАТЧИ
# =========================

@router.message(F.text == "⚽ Матчи")
async def matches_menu(message: Message):

    await message.answer(
        "Выберите лигу 👇",
        reply_markup=leagues_keyboard()
    )


# =========================
# ТАБЛИЦА
# =========================

@router.message(F.text == "📊 Таблица")
async def table_menu(message: Message):

    await message.answer(
        "📊 Таблица пока пустая"
    )


# =========================
# СТАТИСТИКА
# =========================

@router.message(F.text == "📈 Статистика")
async def stats_menu(message: Message):

    await message.answer(
        "📈 Статистика пока пустая"
    )


# =========================
# О БОТЕ
# =========================

@router.message(F.text == "ℹ️ О боте")
async def about_menu(message: Message):

    await message.answer(
        "🤖 MIFL HELPER\n\n"
        "Бот для статистики и матчей MIFL"
    )


# =========================
# ЛИГА
# =========================

@router.callback_query(F.data.startswith("league_"))
async def league_select(callback: CallbackQuery):

    league = callback.data.split("_")[1]

    await callback.message.edit_text(
        "Выберите тур 👇",
        reply_markup=tours_keyboard(league)
    )


# =========================
# ТУР
# =========================

@router.callback_query(F.data.startswith("tour_"))
async def tour_select(callback: CallbackQuery):

    parts = callback.data.split("_")

    league = parts[1]
    tour = int(parts[2])

    matches = await get_matches(league, tour)

    if not matches:

        await callback.message.answer(
            "⚠️ Этот тур ещё не заполнен!"
        )

        return

    text = f"🏆 {league} | Тур {tour}\n\n"

    for match in matches:

        text += (
            f"{match['home_team']} "
            f"{match['home_score']}:{match['away_score']} "
            f"{match['away_team']}\n\n"
        )

    await callback.message.answer(text)
