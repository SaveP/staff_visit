from data_base import db_usersData

# Tamplate dictionary {'telegramId': 123, телеграм id для каждого пользователя бота
#                       'selectedPersons': [1, 2, 5], id выбраных работников
#                       'selectedDirect': 'entry'/'exit'
#                       'timeEnter_mode': True}


# Список где хранится информация о всех пользователях бота
users = list()


def registrationUser(telegramId: int):
    print('Регистрация нового пользователя: ', telegramId)
    db_usersData.add_user(telegramId)


def updateSelectPersons(telegramId, select :int):
    selectList = db_usersData.get_SelectPersons(telegramId)
    if selectList.count(select):
        selectList.remove(select)
        db_usersData.set_SelectPersons(telegramId, selectList)
    else:
        selectList.append(select)
        db_usersData.set_SelectPersons(telegramId, selectList)


def getSelectedPersonal(telegramId):
    return db_usersData.get_SelectPersons(telegramId)


def selectedPersonal_is_empty(telegramId):
    if len(db_usersData.get_SelectPersons(telegramId)) == 0:
        return True
    else:
        return False


def resetSelectedPersonal(telegramId):
    db_usersData.set_SelectPersons(telegramId, ())


def setSelectedDirect(telegramId, dir):
    db_usersData.set_selectedDirect(telegramId, dir)


def resetSelectedDirect(telegramId):
    db_usersData.set_selectedDirect(telegramId, '')


def resetData(telegramId):
    resetSelectedPersonal(telegramId)
    resetSelectedDirect(telegramId)
