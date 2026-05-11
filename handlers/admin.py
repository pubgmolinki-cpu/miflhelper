from aiogram import Router, F
from aiogram.types import Message

router = Router()

# =========================
# 🔐 АДМИН ID (ЗАМЕНИ СВОЙ)
# =========================
ADMIN_ID = 1866813859  # <-- вставь свой Telegram ID


def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID


# =========================
# 📥 /upload команда
# =========================
@router.message(F.text.startswith("/upload"))
async def upload_start(message: Message):

    if not is_admin(message.from_user.id):
        await message.answer("⛔ Нет доступа")
        return

    await message.answer(
        "📄 Отправь файл симуляции матча"
    )


# =========================
# 📄 ПРИЁМ ФАЙЛА
# =========================
@router.message(F.document)
async def handle_simulation_file(message: Message):

    if not is_admin(message.from_user.id):
        return

    # получаем файл
    file = await message.bot.get_file(message.document.file_id)
    downloaded = await message.bot.download_file(file.file_path)

    text = downloaded.read().decode("utf-8")

    await message.answer("⚙️ Обрабатываю симуляцию...")

    # =========================
    # 🔥 ТУТ БУДЕТ ПАРСЕР
    # =========================
    await process_simulation(text)

    await message.answer("✅ Симуляция успешно загружена!")


# =========================
# 🧠 ПАРСЕР (ЗАГЛУШКА)
# =========================
async def process_simulation(text: str):

    lines = text.split("\n")

    league = None
    tour = None

    matches = []

    for line in lines:

        line = line.strip()

        # лига
        if "MIFL" in line or "Кубок" in line:
            league = line
            continue

        # тур
        if "тур" in line.lower():
            try:
                tour = int(''.join(filter(str.isdigit, line)))
            except:
                tour = None
            continue

        # матч
        if ":" in line:

            parts = line.split()

            score_index = None

            for i, p in enumerate(parts):
                if ":" in p:
                    score_index = i
                    break

            if score_index is None:
                continue

            teams = parts[:score_index]
            score = parts[score_index]

            if len(teams) < 2:
                continue

            home_team = teams[0]
            away_team = teams[-1]

            try:
                home_score, away_score = map(int, score.split(":"))
            except:
                continue

            matches.append({
                "league": league,
                "tour": tour,
                "home_team": home_team,
                "away_team": away_team,
                "home_score": home_score,
                "away_score": away_score
            })

    # =========================
    # 💾 ЗДЕСЬ БУДЕТ ЗАПИСЬ В БД
    # =========================

    print("PARSED MATCHES:", matches)
