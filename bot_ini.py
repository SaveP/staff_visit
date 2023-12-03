from aiogram import Bot

# For debug
TOKEN = "6489189653:AAGsrxOBjA0Wy5R444cnwMsSsI-NQjdPMiM"
CHAT_ID = -1001801502361

# For realise
# TOKEN = "6627028597:AAHdR3v2MAoGhSehqvsm35hUSWk6bwzA3aE"
# CHAT_ID = -920858336

# Объект бота
bot = Bot(token=TOKEN)

async def send_message_to_chat(msg):
    await bot.send_message(CHAT_ID, msg)
    return

async def send_message_to_user(telegram_id, msg):
    await bot.send_message(telegram_id, msg)
    return

