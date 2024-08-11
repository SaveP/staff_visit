from aiogram import types, F, Router
import time

import personalList
from keyboards import selectPersons, mainMenu
from bot_ini import send_message_to_chat
import stateInfo
from data_base import db_history, db_event

router = Router()

async def callMainMenu(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Выберите дествие:",
        reply_markup=mainMenu.FullMainMenu()
    )
    await callback.answer()

async def callMainMenuAnswer(callback: types.CallbackQuery):
    await callback.message.answer(
        "Выберите дествие:",
        reply_markup=mainMenu.FullMainMenu()
    )
    await callback.answer()


@router.callback_query(F.data.startswith("main"))
async def callback_main(callback: types.CallbackQuery):
    action = callback.data.split("_")[1]
    place = ''
    try:
        place = callback.data.split("_")[2]
        if place == 'FP':
            place = 'ФП'
        elif place == 'ATI':
            place = 'АТИ'
    except:
        pass


#---------------------------------------

    if action == "entry" or "exit":
        eventInfo = dict()

        named_tuple = time.localtime()  # получить struct_time
        local_time = time.strftime("%H:%M %d/%m/%Y", named_tuple)
        name = personalList.idTel_to_name(callback.from_user.id)
        if name == '':
            name = callback.from_user.username


        if action == "entry":
            direct = "Вход"
        elif action == "exit":
            direct = "Выход"

        msg_for_chat = f"{direct} {place} {local_time} \n{name}"

        eventInfo.update({'TelID': callback.from_user.id,
                          'senderName': callback.from_user.username,
                          'employee_name': name,
                          'direct': action,
                          'time': local_time
                          })

        ret_msg_grup = await send_message_to_chat(msg_for_chat)
        ret_msg = await callback.message.edit_text(msg_for_chat)
        id_event = db_event.add_event(user_id=callback.from_user.id, id_chat=ret_msg.chat.id,
                                      id_msg_chat=ret_msg.message_id, id_grup=ret_msg_grup.chat.id,
                                      id_msg_grup=ret_msg_grup.message_id, description=msg_for_chat,
                                      links="", user_nick=callback.from_user.username, type=action)
        await callback.message.answer(
            "Выберите дествие:",
            reply_markup=mainMenu.FullMainMenu()
        )

        db_history.addEntry(eventInfo['TelID'], eventInfo['senderName'], eventInfo['employee_name'],
                            eventInfo['direct'], eventInfo['time'], id_event)


    elif action == "details":
        stateInfo.resetData(callback.from_user.id)
        await callback.message.edit_text(
            "Выберите людей:",
            reply_markup=selectPersons.selectPersonKb(callback.from_user.id)
        )

    await callback.answer()

#---------------------------------------

    '''if action == "entry":
        eventInfo = dict()

        named_tuple = time.localtime()  # получить struct_time
        local_time = time.strftime("%H:%M %d/%m/%Y", named_tuple)
        name = personalList.idTel_to_name(callback.from_user.id)
        if name == '':
            name = callback.from_user.username



        msg_for_chat = "Вход {} {} \n {}".format(place, local_time, name)

        eventInfo.update({'TelID': callback.from_user.id,
                          'senderName': callback.from_user.username,
                          'employee_name': name,
                          'direct': 'entry',
                          'time': local_time
                          })

        ret_msg_grup = await send_message_to_chat(msg_for_chat)
        ret_msg = await callback.message.edit_text(msg_for_chat)
        id_event = db_event.add_event(user_id=callback.from_user.id, id_chat=ret_msg.chat.id,
                                      id_msg_chat=ret_msg.message_id, id_grup=ret_msg_grup.chat.id,
                                      id_msg_grup=ret_msg_grup.message_id, description=msg_for_chat,
                                      links="", user_nick=callback.from_user.username, type="enter")
        await callback.message.answer(
            "Выберите дествие:",
            reply_markup=mainMenu.FullMainMenu()
        )

        db_history.addEntry(eventInfo['TelID'], eventInfo['senderName'], eventInfo['employee_name'],
                            eventInfo['direct'], eventInfo['time'], id_event)


    elif action == "exit":
        eventInfo = dict()

        named_tuple = time.localtime()  # получить struct_time
        local_time = time.strftime("%H:%M %d/%m/%Y", named_tuple)
        name = personalList.idTel_to_name(callback.from_user.id)
        if name == '':
            name = callback.from_user.username

        msg_for_chat = "Выход {} {} \n {}".format(place, local_time, name)

        eventInfo.update({'TelID': callback.from_user.id,
                          'senderName': callback.from_user.username,
                          'employee_name': name,
                          'direct': 'exit',
                          'time': local_time
                          })

        db_history.addEntry(eventInfo['TelID'], eventInfo['senderName'], eventInfo['employee_name'],
                            eventInfo['direct'], eventInfo['time'])

        await callback.message.edit_text(msg_for_chat)
        await send_message_to_chat(msg_for_chat)
        await callback.message.answer(
            "Выберите дествие:",
            reply_markup=mainMenu.FullMainMenu()
        )'''


