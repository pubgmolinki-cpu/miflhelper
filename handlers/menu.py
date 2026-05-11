from aiogram import Router, F
from aiogram.types import Message

from keyboards import leagues_keyboard

router = Router()


@router.message(F.text == "⚽ Матчи")
async def matches(message: Message):

    await message.answer(
        "Выберите лигу 👇",
        reply_markup=leagues_keyboard()
    )


@router.message(F.text == "📊 Таблица")
async def table(message: Message):

    await message.answer("📊 Таблица пока в разработке")


@router.message(F.text == "📈 Статистика")
async def stats(message: Message):

    await message.answer("📈 Статистика обновляется...")


@router.message(F.text == "ℹ️ О боте")
async def about(message: Message):

    await message.answer(
        "🤖 MIFL HELPER\n"
        "Футбольная лига с симуляцией матчей"
    )
