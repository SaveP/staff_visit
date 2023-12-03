from aiogram import types, F, Router
import time

from bot_ini import send_message_to_chat
from keyboards import otherKeyboards
from hendlers import mainMenu
from data_base import db_history
import stateInfo, personalList

router = Router()

async def callback_kbTime(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Введите время:",
        reply_markup=otherKeyboards.selectTimeKb()
    )

@router.callback_query(F.data.startswith("direct"))
async def callback_select_direct(callback: types.CallbackQuery):
    dir = callback.data.split("_")[1]

    # Обработка нажатия кнопки 'Вход'
    if dir == 'entry':
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

    # Обработка нажатия кнопки 'Cancel'
    if dir == 'Cancel':
        await mainMenu.callMainMenu(callback)
        return
