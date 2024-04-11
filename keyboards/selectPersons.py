from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types

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
    keyboardBuilder.adjust(2, repeat=True)

    keyboardBuilder.row(
        types.InlineKeyboardButton(text='Отмена ❌️', callback_data='selectPersona_Cancel'),
        types.InlineKeyboardButton(text='Далее ➡️', callback_data='selectPersona_Next')
    )

    return keyboardBuilder.as_markup()
