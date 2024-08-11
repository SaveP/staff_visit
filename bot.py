import asyncio
import logging
from aiogram import Dispatcher

import bot_ini
import hendlers.setTime
from bot_ini import bot
from hendlers import start, mainMenu, selectPersons, direct, report_file, other, cancel_move

# Запуск процесса поллинга новых апдейтов
async def main():
    # Включаем логирование, чтобы не пропустить важные сообщения
    logging.basicConfig(level=logging.INFO)

    # Диспетчер
    dp = Dispatcher()

    # Регистрируем роутеры для срабатывания хендлеров
    dp.include_routers(start.router, mainMenu.router, selectPersons.router, direct.router,
                       report_file.router, other.router, hendlers.setTime.router, cancel_move.router)


    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
