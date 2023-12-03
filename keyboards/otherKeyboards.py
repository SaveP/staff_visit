from aiogram.utils.keyboard import InlineKeyboardBuilder

def selectTimeKb():
    # Инициализируем билдер клавиатуры
    keyboardBuilder = InlineKeyboardBuilder()
    keyboardBuilder.button(text='Сейчас', callback_data='time_Now')

    return keyboardBuilder.as_markup()

def selectDirect():
    # Инициализируем билдер клавиатуры
    keyboardBuilder = InlineKeyboardBuilder()
    keyboardBuilder.button(text='Вход', callback_data='direct_entry')
    keyboardBuilder.button(text='Выход', callback_data='direct_exit')
    keyboardBuilder.button(text='Отмена ❌️', callback_data='direct_Cancel')

    keyboardBuilder.adjust(2)

    return keyboardBuilder.as_markup()