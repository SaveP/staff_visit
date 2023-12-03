from aiogram import types

# Клавиатура с кнопками "Вход" "Выход" "Подробнее"
def FullMainMenu():
    buttons = [[
        types.InlineKeyboardButton(text="Я вошёл", callback_data="main_entry"),
        types.InlineKeyboardButton(text="Я вышел", callback_data="main_exit"),
        types.InlineKeyboardButton(text="Подробнее", callback_data="main_details")
    ]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
