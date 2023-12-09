from aiogram import Router
from aiogram.types import Message
from aiogram import F

from keyboards import mainMenu

router = Router()


# Обработчик текстовых сообщений
@router.message(F.text)
async def on_text_message(message: Message):
    text = message.text.lower()

    if text.startswith('вход'):
        words = text.split(' ')
        # Удаляем пустые строки из списка
        while (words.count('')):
            words.remove('')
        msg_to_chat = ''
        print(words)

    else:
        await message.answer('Мне нечего на это ответить(')
        await message.answer(
            "Выберите дествие:",
            reply_markup=mainMenu.FullMainMenu()
        )
