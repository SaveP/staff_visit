from aiogram import types, F, Router
import datetime
import time

from bot_ini import send_message_to_chat
from keyboards import otherKeyboards
from hendlers import mainMenu
from data_base import db_history, db_event
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


@router.callback_query(F.data.startswith("direct"))
async def callback_select_direct(callback: types.CallbackQuery):

    #Парсинг данных о площадке на которую был совершён вход/выход
    dir = callback.data.split("_")[1]
    place = ''
    try:
        place = callback.data.split("_")[2]
        if place == 'FP':
            place = 'ФП'
        elif place == 'ATI':
            place = 'АТИ'
    except:
        pass

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


    # Обработка нажатия кнопки 'Вход'
    if dir == 'entry' or dir == 'exit':

        entered_time = ""
        if stateInfo.get_enter_time_mod(callback.from_user.id) == 'disable':
            entered_time = time.strftime("%H:%M %d/%m/%Y", time.localtime())
        elif stateInfo.get_enter_time_mod(callback.from_user.id) == 'enable':
            sel_time = stateInfo.get_enter_time(callback.from_user.id)
            entered_time = get_last_date(sel_time)

        names = " ".join(personalList.getNames(stateInfo.getSelectedPersonal(callback.from_user.id)))

        ru_dir = "dir"
        if dir == 'entry':
            ru_dir = 'Вход'
        elif dir == 'exit':
            ru_dir = 'Выход'
        msg_for_chat = f"{ru_dir} {place} {entered_time} \n{names}"

        selectedEmployees = personalList.getNames(stateInfo.getSelectedPersonal(callback.from_user.id))
        eventInfo = dict()


        ret_msg_grup = await send_message_to_chat(msg_for_chat)
        ret_msg = await callback.message.edit_text(msg_for_chat)
        id_event = db_event.add_event(user_id=callback.from_user.id, id_chat=ret_msg.chat.id,
                                      id_msg_chat=ret_msg.message_id, id_grup=ret_msg_grup.chat.id,
                                      id_msg_grup=ret_msg_grup.message_id, description=msg_for_chat,
                                      links="", user_nick=callback.from_user.username, type=dir)

        for emloyeesName in selectedEmployees:
            eventInfo.clear()
            eventInfo.update({'TelID': callback.from_user.id,
                              'senderName': callback.from_user.username,
                              'employee_name': emloyeesName,
                              'direct': dir,
                              'time': entered_time
                              })
            db_history.addEntry(eventInfo['TelID'], eventInfo['senderName'], eventInfo['employee_name'],
                                eventInfo['direct'], eventInfo['time'], id_event)

        await mainMenu.callMainMenuAnswer(callback)
        return


    # Обработка нажатия кнопки 'Cancel'
    if dir == 'Cancel':
        stateInfo.resetData(callback.from_user.id)
        await mainMenu.callMainMenu(callback)
        return
