from data_base import db_usersData

# Tamplate dictionary {'telegramId': 123, телеграм id для каждого пользователя бота
#                       'selectedPersons': [1, 2, 5], id выбраных работников
#                       'selectedDirect': 'entry'/'exit'
#                       'timeEnter_mode': 'enable'/'disable'}


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


def get_enter_time_mod(telegramId: int):
    return db_usersData.get_TimeEnterMode(telegramId)


def set_enter_time_mod_on(telegramId: int):
    db_usersData.set_TimeEnterMode(telegramId, 'enable')


def set_enter_time_mod_off(telegramId: int):
    db_usersData.set_TimeEnterMode(telegramId, 'disable')


def change_enter_time_mod(telegramId: int):
    mode = get_enter_time_mod(telegramId)
    if mode == 'disable':
        set_enter_time_mod_on(telegramId)
    else:
        set_enter_time_mod_off(telegramId)


def get_enter_time(telegramId: int, par=''):
    if par == 'h':
        time = db_usersData.get_enter_time(telegramId)
        h = time.split(':')[0]
        return h
    elif par == 'm':
        time = db_usersData.get_enter_time(telegramId)
        m = time.split(':')[1]
        return m
    else:
        return db_usersData.get_enter_time(telegramId)


def set_enter_time(telegramId: int, time: str = '', h=None, m=None):
    if (h == None) and (m == None):
        db_usersData.set_enter_time(telegramId, time)
    elif (h != None) and (m != None):
        db_usersData.set_enter_time(telegramId, f'{str(h)}:{str(m)}')
    elif h == None:
        h = get_enter_time(telegramId).split(':')[0]
        db_usersData.set_enter_time(telegramId, f'{str(h)}:{str(m)}')
    elif m == None:
        m = get_enter_time(telegramId).split(':')[1]
        db_usersData.set_enter_time(telegramId, f'{str(h)}:{str(m)}')


def reset_enter_time(telegramId: int):
    set_enter_time(telegramId, ':')


def resetData(telegramId):
    resetSelectedPersonal(telegramId)
    resetSelectedDirect(telegramId)
    set_enter_time_mod_off(telegramId)
    reset_enter_time(telegramId)
