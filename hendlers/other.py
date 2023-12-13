from aiogram import types, Router
from aiogram.filters.command import Command

from keyboards import mainMenu


router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    msg = "Добро пожаловать в бот посещения персонала Тавриды.\n" \
          "Если у Вас возникнут сложности с использованием этого бота, воспользуйтесь командой /help"

    await message.answer(msg)
    await message.answer(
        "Выберите дествие:",
        reply_markup=mainMenu.FullMainMenu()
    )


@router.message(Command("help"))
async def cmd_start(message: types.Message):
    msg = '''Привет. Я бот который помогает следить за твоим входом и выходом с площадки Тавриды.
    Если ты прошёл через КПП в одиночку, то просто нажми кнопку "Вход" или "Выход". Время прохода выставится автоматически.
    Если ты прошёл КПП с коллегами, то можешь нажать "Подробнее" и выбрать своё имя и имена коллег, а затем нажать "Вход" или "Выход".
    Так же, во вкладке "Подробнее" есть функция выбора времени. Если ты забыл вовремя отметиться в боте, то у тебя есть на это сутки).'''

    await message.answer(msg)
    await message.answer(
        "Выберите дествие:",
        reply_markup=mainMenu.FullMainMenu()
    )

'''@router.message(Command("message_for_all"))
async def cmd_start(message: types.Message):
    msg = message.text

    await message.answer(msg)
    await message.answer(
        "Выберите дествие:",
        reply_markup=mainMenu.FullMainMenu()
    )'''
