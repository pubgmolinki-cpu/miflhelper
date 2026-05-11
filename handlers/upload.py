from aiogram import Router, F
from aiogram.types import Message, Document

from database import pool

router = Router()


@router.message(F.document)
async def handle_file(message: Message, document: Document):

    file = await message.bot.get_file(document.file_id)
    file_path = file.file_path

    downloaded = await message.bot.download_file(file_path)

    text = downloaded.read().decode("utf-8")

    await parse_and_save(text)

    await message.answer("✅ Симуляция загружена и обработана!")


# =========================
# ПАРСЕР СИМУЛЯЦИИ
# =========================

async def parse_and_save(text: str):

    lines = text.split("\n")

    league = None
    tour = None

    matches = []

    for line in lines:

        line = line.strip()

        if "MIFL" in line or "Кубок" in line:

            league = line
            continue

        if "тур" in line.lower():

            tour = int(''.join(filter(str.isdigit, line)))
            continue

        if ":" in line and "-" not in line:

            parts = line.split()

            score_index = None

            for i, p in enumerate(parts):

                if ":" in p:

                    score_index = i
                    break

            teams = parts[:score_index]
            score = parts[score_index]

            home_team = teams[0]
            away_team = teams[-1]

            home_score, away_score = map(int, score.split(":"))

            matches.append((
                league,
                tour,
                home_team,
                away_team,
                home_score,
                away_score
            ))

    async with pool.acquire() as conn:

        for m in matches:

            await conn.execute("""
                INSERT INTO matches
                (league, tour, home_team, away_team, home_score, away_score)
                VALUES ($1,$2,$3,$4,$5,$6)
            """, *m)
