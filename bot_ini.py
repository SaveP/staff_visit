from aiogram import Bot

# For debug
TOKEN = 
CHAT_ID = -1001801502361

# For realise
#TOKEN = 
#CHAT_ID = -920858336

# Объект бота
bot = Bot(token=TOKEN)

async def send_message_to_chat(msg: str):
    await bot.send_message(CHAT_ID, msg)
    return

async def send_message_to_user(telegram_id, msg):
    await bot.send_message(telegram_id, msg)
    return
