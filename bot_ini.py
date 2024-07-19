from aiogram import Bot
from config import Config, load_config


config: Config = load_config()
TOKEN: str = config.tg_bot.token
CHAT_ID: str = config.tg_bot.chat_id

# Объект бота
bot = Bot(token=TOKEN)

async def send_message_to_chat(msg: str):
    await bot.send_message(CHAT_ID, msg)
    return

async def send_message_to_user(telegram_id, msg):
    await bot.send_message(telegram_id, msg)
    return
