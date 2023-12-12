from aiogram import types, F, Router
import datetime
import time

from bot_ini import send_message_to_chat
from keyboards import otherKeyboards
from hendlers import mainMenu
from data_base import db_history
import stateInfo, personalList

#Функция принимает время в формате строки "%H:%M" и возвращает дату когда последний раз было это время
def get_last_date(time: str):
    time_now = datetime.datetime.now()
    date = datetime.datetime.strptime(f'{time} {time_now.day}/{time_now.month}/{time_now.year}', '%H:%M %d/%m/%Y')
    if date >= time_now:
        one_day = datetime.timedelta(days=1)
        date = date - one_day
    return date.strftime('%H:%M %d/%m/%Y')


router = Router()

'''async def callback_kbTime(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Введите время:",
        reply_markup=otherKeyboards.selectTimeKb()
    )'''

@router.callback_query(F.data.startswith("direct"))
async def callback_select_direct(callback: types.CallbackQuery):


    dir = callback.data.split("_")[1]
    # Обработка нажатия кнопки с часиками
    if dir == 'timeEnter':
        stateInfo.change_enter_time_mod(callback.from_user.id)
        if stateInfo.get_enter_time_mod(callback.from_user.id)=='enable':
            phrase = 'Выберите время, а затем нажмите Вход или Выход'
        else:
            phrase = 'Выберите действие:'

        await callback.message.edit_text(
            phrase,
            reply_markup=otherKeyboards.selectDirect(callback.from_user.id)
        )

    # Обработка нажатия кнопки 'Вход' при автоматическом выборе времени
    if (dir == 'entry') and (stateInfo.get_enter_time_mod(callback.from_user.id) == 'disable'):
        named_tuple = time.localtime()  # получить struct_time
        local_time = time.strftime("%H:%M %d/%m/%Y", named_tuple)
        names = " ".join(personalList.getNames(stateInfo.getSelectedPersonal(callback.from_user.id)))
        msg_for_chat = "Вход {} \n {}".format(local_time, names)


        selectedEmployees = personalList.getNames(stateInfo.getSelectedPersonal(callback.from_user.id))
        for emloyeesName in selectedEmployees:
            eventInfo = dict()
            eventInfo.update({'TelID': callback.from_user.id,
                              'senderName': callback.from_user.username,
                              'employee_name': emloyeesName,
                              'direct': 'entry',
                              'time': local_time
                              })

            db_history.addEntry(eventInfo['TelID'], eventInfo['senderName'], eventInfo['employee_name'],
                                eventInfo['direct'], eventInfo['time'])

        await callback.message.edit_text(msg_for_chat)
        await send_message_to_chat(msg_for_chat)
        await mainMenu.callMainMenuAnswer(callback)
        return


    # Обработка нажатия кнопки 'Вход' при ручном выборе времени
    if (dir == 'entry') and (stateInfo.get_enter_time_mod(callback.from_user.id) == 'enable'):

        sel_time = stateInfo.get_enter_time(callback.from_user.id)

        entered_time = get_last_date(sel_time)
        names = " ".join(personalList.getNames(stateInfo.getSelectedPersonal(callback.from_user.id)))
        msg_for_chat = "Вход {} \n {}".format(entered_time, names)

        selectedEmployees = personalList.getNames(stateInfo.getSelectedPersonal(callback.from_user.id))
        for emloyeesName in selectedEmployees:
            eventInfo = dict()

            eventInfo.update({'TelID': callback.from_user.id,
                              'senderName': callback.from_user.username,
                              'employee_name': emloyeesName,
                              'direct': 'entry',
                              'time': entered_time
                              })

            db_history.addEntry(eventInfo['TelID'], eventInfo['senderName'], eventInfo['employee_name'],
                                eventInfo['direct'], eventInfo['time'])

        await callback.message.edit_text(msg_for_chat)
        await send_message_to_chat(msg_for_chat)
        await mainMenu.callMainMenuAnswer(callback)
        return


    # Обработка нажатия кнопки 'Выход'
    if dir == 'exit':
        named_tuple = time.localtime()  # получить struct_time
        local_time = time.strftime("%H:%M %d/%m/%Y", named_tuple)
        names = " ".join(personalList.getNames(stateInfo.getSelectedPersonal(callback.from_user.id)))
        msg_for_chat = "Выход {} \n {}".format(local_time, names)

        selectedEmployees = personalList.getNames(stateInfo.getSelectedPersonal(callback.from_user.id))
        for emloyeesName in selectedEmployees:
            eventInfo = dict()

            eventInfo.update({'TelID': callback.from_user.id,
                              'senderName': callback.from_user.username,
                              'employee_name': emloyeesName,
                              'direct': 'exit',
                              'time': local_time
                              })

            db_history.addEntry(eventInfo['TelID'], eventInfo['senderName'], eventInfo['employee_name'],
                                eventInfo['direct'], eventInfo['time'])

        await callback.message.edit_text(msg_for_chat)
        await send_message_to_chat(msg_for_chat)
        await mainMenu.callMainMenuAnswer(callback)
        return

    # Обработка нажатия кнопки 'Вход' при ручном выборе времени
    if (dir == 'exit') and (stateInfo.get_enter_time_mod(callback.from_user.id) == 'enable'):
        sel_time = stateInfo.get_enter_time(callback.from_user.id)
        entered_time = get_last_date(sel_time)
        names = " ".join(personalList.getNames(stateInfo.getSelectedPersonal(callback.from_user.id)))
        msg_for_chat = "Выход {} \n {}".format(entered_time, names)

        selectedEmployees = personalList.getNames(stateInfo.getSelectedPersonal(callback.from_user.id))
        for emloyeesName in selectedEmployees:
            eventInfo = dict()

            eventInfo.update({'TelID': callback.from_user.id,
                              'senderName': callback.from_user.username,
                              'employee_name': emloyeesName,
                              'direct': 'exit',
                              'time': entered_time
                              })

            db_history.addEntry(eventInfo['TelID'], eventInfo['senderName'], eventInfo['employee_name'],
                                eventInfo['direct'], eventInfo['time'])

        await callback.message.edit_text(msg_for_chat)
        await send_message_to_chat(msg_for_chat)
        await mainMenu.callMainMenuAnswer(callback)
        return

    # Обработка нажатия кнопки 'Cancel'
    if dir == 'Cancel':
        await mainMenu.callMainMenu(callback)
        return
