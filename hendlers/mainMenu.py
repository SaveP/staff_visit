from aiogram import types, F, Router
import time

import personalList
from keyboards import selectPersons, mainMenu
from bot_ini import send_message_to_chat
import stateInfo
from data_base import db_history

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

    if action == "entry":
        eventInfo = dict()

        named_tuple = time.localtime()  # получить struct_time
        local_time = time.strftime("%H:%M %d/%m/%Y", named_tuple)
        name = personalList.idTel_to_name(callback.from_user.id)
        if name == '':
            name = callback.from_user.username

        msg_for_chat = "Вход {} \n {}".format(local_time, name)

        eventInfo.update({'TelID': callback.from_user.id,
                          'senderName': callback.from_user.username,
                          'employee_name': name,
                          'direct': 'entry',
                          'time': local_time
                          })

        db_history.addEntry(eventInfo['TelID'], eventInfo['senderName'], eventInfo['employee_name'],
                            eventInfo['direct'], eventInfo['time'])

        await send_message_to_chat(msg_for_chat)
        await callback.message.edit_text(msg_for_chat)
        await callback.message.answer(
            "Выберите дествие:",
            reply_markup=mainMenu.FullMainMenu()
        )

    elif action == "exit":
        eventInfo = dict()

        named_tuple = time.localtime()  # получить struct_time
        local_time = time.strftime("%H:%M %d/%m/%Y", named_tuple)
        name = personalList.idTel_to_name(callback.from_user.id)
        if name == '':
            name = callback.from_user.username

        msg_for_chat = "Выход {} \n {}".format(local_time, name)

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
        )

    elif action == "details":
        stateInfo.resetData(callback.from_user.id)
        await callback.message.edit_text(
            "Выберите людей:",
            reply_markup=selectPersons.selectPersonKb(callback.from_user.id)
        )

    await callback.answer()
