from aiogram.utils.keyboard import InlineKeyboardBuilder

# Клавиатура с кнопками "Вход" "Выход" "Подробнее"
def FullMainMenu():
    keyboard = InlineKeyboardBuilder()
    keyboard.button(text="Я вошёл ФП", callback_data="main_entry_FP")
    keyboard.button(text="Я вышел ФП", callback_data="main_exit_FP")
    keyboard.button(text="Я вошёл АТИ", callback_data="main_entry_ATI")
    keyboard.button(text="Я вошёл АТИ", callback_data="main_exit_ATI")
    keyboard.button(text="Подробнее", callback_data="main_details")
    keyboard.adjust(2, 2, 1)

    return keyboard.as_markup()
