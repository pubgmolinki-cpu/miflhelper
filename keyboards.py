from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# =======================
# ГЛАВНОЕ МЕНЮ (НИЖНИЕ КНОПКИ)
# =======================

def main_menu():

    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="⚽ Матчи"),
                KeyboardButton(text="📊 Таблица")
            ],
            [
                KeyboardButton(text="📈 Статистика"),
                KeyboardButton(text="ℹ️ О боте")
            ]
        ],
        resize_keyboard=True
    )

# =======================
# ЛИГИ (INLINE)
# =======================

def leagues_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="MIFL", callback_data="league_MIFL")
            ],
            [
                InlineKeyboardButton(text="Кубок Меридианы", callback_data="league_MERIDIAN")
            ],
            [
                InlineKeyboardButton(text="Кубок Первенства", callback_data="league_FIRST")
            ]
        ]
    )

# =======================
# ТУРЫ (INLINE)
# =======================

def tours_keyboard(league):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="1 тур", callback_data=f"tour_{league}_1"),
                InlineKeyboardButton(text="2 тур", callback_data=f"tour_{league}_2")
            ],
            [
                InlineKeyboardButton(text="3 тур", callback_data=f"tour_{league}_3"),
                InlineKeyboardButton(text="4 тур", callback_data=f"tour_{league}_4")
            ],
            [
                InlineKeyboardButton(text="5 тур", callback_data=f"tour_{league}_5"),
                InlineKeyboardButton(text="6 тур", callback_data=f"tour_{league}_6")
            ],
            [
                InlineKeyboardButton(text="7 тур", callback_data=f"tour_{league}_7")
            ]
        ]
    )
