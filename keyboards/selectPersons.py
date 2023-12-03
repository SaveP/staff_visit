from aiogram.utils.keyboard import InlineKeyboardBuilder

import personalList, stateInfo

def selectPersonKb(telegramId):
    # Инициализируем билдер клавиатуры
    keyboardBuilder = InlineKeyboardBuilder()
    # Фильтруем только те которые нужно отображать
    persons = [x for x in personalList.getStaff() if x['View'] == 'visible']
    # Создаём набор кнопок
    for per in persons:
        # Если этот сотрудник был выбран, то он будет помечен галочкой
        iconSel = ''

        if stateInfo.getSelectedPersonal(telegramId).count(per['ID']):
            iconSel = '✅ '

        keyboardBuilder.button(text=iconSel + per['Name'], callback_data='selectPersona_%s' % per['ID'])

    # Групируем кнопки по 2 в ряд
    keyboardBuilder.adjust(2)

    keyboardBuilder.button(text='Отмена ❌️', callback_data='selectPersona_Cancel')
    keyboardBuilder.button(text='Далее ➡️', callback_data='selectPersona_Next')
    keyboardBuilder.adjust(2)

    return keyboardBuilder.as_markup()
