from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards import main_menu

router = Router()

@router.callback_query(F.data == "back_main")
async def back_main(callback: CallbackQuery):

    await callback.message.edit_text(
        "🏠 Главное меню",
        reply_markup=main_menu()
    )
