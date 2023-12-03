from aiogram import types, Router
from aiogram.filters.command import Command

import stateInfo
from keyboards import mainMenu

from aiogram.types import FSInputFile

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    stateInfo.registrationUser(message.from_user.id)
    stateInfo.resetData(message.from_user.id)
    msg = "Добро пожаловать в бот посещения персонала Тавриды.\n" \
          "Если у Вас возникнут сложности с использованием этого бота, обратитесь в администрацию президента."

    await message.answer(msg)
    await message.answer(
        "Выберите дествие:",
        reply_markup=mainMenu.FullMainMenu()
    )
