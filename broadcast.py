from bot_ini import send_message_to_user
from data_base.db_usersData import get_allUsers


def send_message_to_all_users(msg: str):
    for id_user in [i[0] for i in get_allUsers()]:
        try:
            print(msg, id_user)
            send_message_to_user(id_user, msg)
        except ValueError:
            print('Ошибка при отправке сообщения пользователю ', id_user)
            print(ValueError)
