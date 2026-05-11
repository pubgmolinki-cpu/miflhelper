from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def main_menu():

    return InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(
                    text="Матчи ⚽",
                    callback_data="matches"
                )
            ],

            [
                InlineKeyboardButton(
                    text="Таблица 📊",
                    callback_data="table"
                )
            ],

            [
                InlineKeyboardButton(
                    text="Статистика 📈",
                    callback_data="stats"
                )
            ],

            [
                InlineKeyboardButton(
                    text="О боте ℹ️",
                    callback_data="about"
                )
            ]

        ]
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

    keyboard = []

    for i in range(1, 8):

        keyboard.append([
            InlineKeyboardButton(
                text=f"{i} тур",
                callback_data=f"tour_{league}_{i}"
            )
        ])

    return InlineKeyboardMarkup(
        inline_keyboard=keyboard
    )
