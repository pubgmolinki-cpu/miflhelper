from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config import ADMIN_ID
from parser import parse_match
from database import add_match

router = Router()

waiting_admin = {}

@router.message(Command("add"))
async def add_sim(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    waiting_admin[message.from_user.id] = True

    await message.answer(
        "Отправьте симуляцию матча."
    )

@router.message()
async def handle_sim(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    if message.from_user.id not in waiting_admin:
        return

    parsed = parse_match(message.text)

    if not parsed:

        await message.answer(
            "❌ Не удалось распарсить матч!"
        )

        return

    await add_match(
        league="MIFL",
        tour=1,
        home_team=parsed["home_team"],
        away_team=parsed["away_team"],
        home_score=parsed["home_score"],
        away_score=parsed["away_score"],
        raw_text=message.text
    )

    await message.answer(
        "✅ Матч добавлен!"
    )

    del waiting_admin[message.from_user.id]
