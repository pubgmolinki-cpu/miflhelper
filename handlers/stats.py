from aiogram import Router, F
from aiogram.types import CallbackQuery

from database import pool

router = Router()

@router.callback_query(F.data == "stats")
async def stats_handler(callback: CallbackQuery):

    async with pool.acquire() as conn:

        rows = await conn.fetch("""
            SELECT player_name, goals, assists, motm
            FROM players
            ORDER BY goals DESC
            LIMIT 10
        """)

    if not rows:

        await callback.message.answer(
            "📊 Пока нет статистики игроков!"
        )
        return

    text = "📈 <b>Топ игроков MIFL</b>\n\n"

    pos = 1

    for r in rows:

        text += (
            f"{pos}. {r['player_name']}\n"
            f"⚽ Голы: {r['goals']}\n"
            f"🎯 Ассисты: {r['assists']}\n"
            f"🌟 MOTM: {r['motm']}\n\n"
        )

        pos += 1

    await callback.message.answer(text)
