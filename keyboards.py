from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


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


def leagues_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="MIFL",
                    callback_data="league_MIFL"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Кубок Меридианы",
                    callback_data="league_MERIDIAN"
                )
            ],
            [
                InlineKeyboardButton(
                    text="Кубок Первенства",
                    callback_data="league_FIRST"
                )
            ]
        ]
    )


def tours_keyboard(league):

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="1 тур",
                    callback_data=f"tour_{league}_1"
                ),

                InlineKeyboardButton(
                    text="2 тур",
                    callback_data=f"tour_{league}_2"
                )
            ],
            [
                InlineKeyboardButton(
                    text="3 тур",
                    callback_data=f"tour_{league}_3"
                ),

                InlineKeyboardButton(
                    text="4 тур",
                    callback_data=f"tour_{league}_4"
                )
            ]
        ]
    )
