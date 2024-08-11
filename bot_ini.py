from aiogram import Bot
from config import Config, load_config


config: Config = load_config()
TOKEN: str = config.tg_bot.token
CHAT_ID: str = config.tg_bot.chat_id

# Объект бота
bot = Bot(token=TOKEN)


async def delete_msg(chat_id: int, message_id: int):
    await bot.delete_message(chat_id, message_id)
    return


async def send_message_to_chat(msg: str):
    ret = await bot.send_message(CHAT_ID, msg)
    return ret


async def send_message_to_user(telegram_id, msg):
    ret = await bot.send_message(telegram_id, msg)
    return ret
