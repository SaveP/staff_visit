from aiogram.utils.keyboard import InlineKeyboardBuilder
import stateInfo

'''def selectTimeKb(tel_id: int):
    # Инициализируем билдер клавиатуры
    keyboardBuilder = InlineKeyboardBuilder()
    keyboardBuilder.button(text='Вход', callback_data='direct_entry')
    keyboardBuilder.button(text='Выход', callback_data='direct_exit')
    if stateInfo.get_enter_time_mod(tel_id) == 'enable':
        keyboardBuilder.button(text='✅ 🕛', callback_data='direct_timeEnter')
    else:
        keyboardBuilder.button(text='🕛', callback_data='direct_timeEnter')
    keyboardBuilder.button(text='Отмена ❌️', callback_data='direct_Cancel')
    keyboardBuilder.button(text='Сейчас', callback_data='time_Now')

    for i in range(24):
        keyboardBuilder.button(text=f'{str(i)}:', callback_data=f'time_hour_{i}')
    for i in range(0, 60, 5):
        keyboardBuilder.button(text=f':{str(i)}', callback_data=f'time_min_{i}')

    keyboardBuilder.adjust(3, 1, 6)

    return keyboardBuilder.as_markup()'''

def selectDirect(tel_id: int):
    # Инициализируем билдер клавиатуры
    keyboardBuilder = InlineKeyboardBuilder()
    keyboardBuilder.button(text='Вход', callback_data='direct_entry')
    keyboardBuilder.button(text='Выход', callback_data='direct_exit')

    #Если нажаты часы то открывается таблица выбора времени
    if stateInfo.get_enter_time_mod(tel_id) == 'enable':
        keyboardBuilder.button(text='✅ 🕛', callback_data='direct_timeEnter')

        for i in range(24):
            sel = ''
            if stateInfo.get_enter_time(tel_id, 'h') == str(i):
                sel = '✅'
            keyboardBuilder.button(text=f'{sel}{str(i)}:', callback_data=f'time_hour_{i}')
        for i in range(0, 60, 5):
            sel = ''
            if stateInfo.get_enter_time(tel_id, 'm') == str(i):
                sel = '✅'
            keyboardBuilder.button(text=f'{sel}{str(i)}:', callback_data=f'time_min_{i}')

        keyboardBuilder.button(text='Отмена ❌️', callback_data='direct_Cancel')

        keyboardBuilder.adjust(3, 6)

    else:
        keyboardBuilder.button(text='🕛', callback_data='direct_timeEnter')

        keyboardBuilder.button(text='Отмена ❌️', callback_data='direct_Cancel')

        keyboardBuilder.adjust(3, 1)

    return keyboardBuilder.as_markup()



