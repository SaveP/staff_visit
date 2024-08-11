from aiogram import types, Router
from bot_ini import delete_msg
from data_base import db_event

from aiogram import F

router = Router()

@router.message(F.text.lower() == "отмена")
async def cancel_move(message: types.Message):
    reply_msg = message.reply_to_message

    event = db_event.find_event(reply_msg.chat.id, reply_msg.message_id)

    description = f"Отмена перемещения.\n{event}"
    db_event.add_event(user_id=message.from_user.id, id_chat=message.chat.id, id_msg_chat=message.message_id,
                       user_nick=message.from_user.username, type="cancel_entry", description=description)

    #Удаляем сообщение из личного чата с ботом
    await delete_msg(event['id_chat'], event['id_msg_chat'])

    #Удаляем сообщение из группы
    await delete_msg(event['id_grup'], event['id_msg_grup'])

    await delete_msg(message.chat.id, message.message_id)
