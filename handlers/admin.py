from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config import ADMIN_ID

from parser import parse_match

from database import add_match

from services.standings import (
    update_standings
)

from services.player_parser import (
    extract_goalscorers,
    extract_assisters
)

from services.player_service import (
    add_goal,
    add_assist
)

router = Router()

waiting_admin = {}

@router.message(Command("add"))
async def add_sim(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    waiting_admin[
        message.from_user.id
    ] = True

    await message.answer(
        "📥 Отправьте симуляцию матча."
    )

@router.message()
async def handle_sim(message: Message):

    if message.from_user.id != ADMIN_ID:
        return

    if message.from_user.id not in waiting_admin:
        return

    parsed = parse_match(
        message.text
    )

    if not parsed:

        await message.answer(
            "❌ Ошибка парсинга!"
        )

        return

    league = "MIFL"
    tour = 1

    await add_match(

        league=league,
        tour=tour,

        home_team=parsed["home_team"],
        away_team=parsed["away_team"],

        home_score=parsed["home_score"],
        away_score=parsed["away_score"],

        raw_text=message.text

    )

    await update_standings(

        league=league,

        home_team=parsed["home_team"],
        away_team=parsed["away_team"],

        home_score=parsed["home_score"],
        away_score=parsed["away_score"]

    )

    scorers = extract_goalscorers(
        message.text
    )

    for scorer in scorers:

        await add_goal(
            scorer
        )

    assisters = extract_assisters(
        message.text
    )

    for assist in assisters:

        await add_assist(
            assist
        )

    await message.answer(
        "✅ Матч обработан!"
    )

    del waiting_admin[
        message.from_user.id
    ]
