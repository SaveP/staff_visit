from aiogram.utils.keyboard import InlineKeyboardBuilder
import stateInfo


def selectDirect(tel_id: int):
    # Инициализируем билдер клавиатуры
    keyboardBuilder = InlineKeyboardBuilder()
    '''keyboardBuilder.button(text='Вход', callback_data='direct_entry')
    keyboardBuilder.button(text='Выход', callback_data='direct_exit')'''
    keyboardBuilder.button(text="Вход ФП", callback_data="direct_entry_FP")
    keyboardBuilder.button(text="Выход ФП", callback_data="direct_exit_FP")
    keyboardBuilder.button(text="Вход АТИ", callback_data="direct_entry_ATI")
    keyboardBuilder.button(text="Выход АТИ", callback_data="direct_exit_ATI")

    #Если нажаты часы то открывается таблица выбора времени
    if stateInfo.get_enter_time_mod(tel_id) == 'enable':
        #keyboardBuilder.button(text='✅ 🕛', callback_data='direct_timeEnter')

        for i in range(24):
            sel = ''
            if stateInfo.get_enter_time(tel_id, 'h') == str(i):
                sel = '✅'
            keyboardBuilder.button(text=f'{sel}{str(i)}:', callback_data=f'time_hour_{i}')
        for i in range(0, 60, 5):
            sel = ''
            if stateInfo.get_enter_time(tel_id, 'm') == str(i):
                sel = '✅'
            keyboardBuilder.button(text=f'{sel}:{str(i)}', callback_data=f'time_min_{i}')

        keyboardBuilder.button(text='Отмена ❌️', callback_data='direct_Cancel')

        keyboardBuilder.adjust(2, 2, 6)

    else:
        keyboardBuilder.button(text='🕛', callback_data='direct_timeEnter')

        keyboardBuilder.button(text='Отмена ❌️', callback_data='direct_Cancel')

        keyboardBuilder.adjust(2, 2, 1)

    return keyboardBuilder.as_markup()



