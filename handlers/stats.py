from aiogram import Router, F
from aiogram.types import Message

from database import pool

router = Router()

@router.message(F.text == "📈 Статистика")
async def stats(message: Message):

    async with pool.acquire() as conn:

        rows = await conn.fetch("""
            SELECT player_name, goals, assists
            FROM players
            ORDER BY goals DESC
            LIMIT 10
        """)

    if not rows:
        await message.answer("📊 Статистика пока пустая!")
        return

    text = "📈 <b>Топ игроков</b>\n\n"

    i = 1

    for r in rows:

        text += (
            f"{i}. {r['player_name']}\n"
            f"⚽ {r['goals']} | 🎯 {r['assists']}\n\n"
        )

        i += 1

    await message.answer(text)
