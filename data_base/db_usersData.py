import sqlite3 as sq

with sq.connect('staffBotDb.db') as con:
    cur = con.cursor()

# Tamplate dictionary {'telegramId': 123, телеграм id для каждого пользователя бота
#                       'selectedPersons': '1, 2, 5', id выбраных работников
#                       'selectedDirect': 'entry'/'exit'
#                       'timeEnter_mode': 'enable'/'disable'}

#cur.execute('DROP TABLE users')

cur.execute("""CREATE TABLE IF NOT EXISTS users(
                telegram_id INTEGER,
                selectedPersonsID TEXT,
                selectedDirect TEXT,
                timeEnter_mode TEXT DEFAULT "disable",
                enter_time TEXT DEFAULT ":"
                )""")

con.commit()

def get_allUsers():
    with sq.connect('staffBotDb.db') as con:
        cur = con.cursor()

    cur.execute('SELECT * FROM users')
    data = cur.fetchall()
    con.commit()
    return data


def get_userData(telID: int):
    with sq.connect('staffBotDb.db') as con:
        cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE telegram_id = "{telID}"')
    data = cur.fetchone()
    con.commit()

    if data == None:
        print('None')
        return False
    return data

def add_user(telID: int, selectedPersonsID = '', selectedDirect='None', timeEnter_mode='disable'):
    if get_userData(telID):
        print(f'Пользователь с ID {telID} уже есть в базе данных')
        return False

    with sq.connect('staffBotDb.db') as con:
        cur = con.cursor()

    sqlite_insert_with_param = '''INSERT INTO users (telegram_id, selectedPersonsID, selectedDirect, timeEnter_mode)
                                VALUES(?, ?, ?, ?)'''
    data_tuple = (telID, selectedPersonsID, selectedDirect, timeEnter_mode)
    cur.execute(sqlite_insert_with_param, data_tuple)

    con.commit()


def set_SelectPersons(telID: int, selectedPersons: tuple):
    # Преобразуем список selectedPersons в строку
    str_selected = ','.join(map(str, selectedPersons))

    with sq.connect('staffBotDb.db') as con:
        cur = con.cursor()
    sqlite_insert_with_param = "UPDATE users SET selectedPersonsID = ? WHERE telegram_id = ?"
    data_tuple = (str_selected, telID)
    cur.execute(sqlite_insert_with_param, data_tuple)
    con.commit()


def get_SelectPersons(telID: int):
    with sq.connect('staffBotDb.db') as con:
        cur = con.cursor()

    cur.execute(f'SELECT users.selectedPersonsID FROM users WHERE telegram_id = {telID}')
    data = cur.fetchone()[0]
    con.commit()

    if data == '':
        return []

    # Разделяем строку из БД по разделителю ',' и преобразуем символы в int
    data = data.split(',')
    data = [int(i) for i in data]

    return data


def get_selectedDirect(telID: int):
    with sq.connect('staffBotDb.db') as con:
        cur = con.cursor()

    cur.execute(f'SELECT users.selectedDirect FROM users WHERE telegram_id = {telID}')
    dir = cur.fetchone()[0]
    con.commit()

    return dir


def set_selectedDirect(telID: int, dir: str):
    with sq.connect('staffBotDb.db') as con:
        cur = con.cursor()

    cur.execute("UPDATE users SET selectedDirect = ? WHERE telegram_id = ?", (dir, telID))
    con.commit()


def set_TimeEnterMode(telID: int, mode: str):
    with sq.connect('staffBotDb.db') as con:
        cur = con.cursor()

    cur.execute("UPDATE users SET timeEnter_mode = ? WHERE telegram_id = ?", (mode, telID))
    con.commit()


def get_TimeEnterMode(telID: int):
    with sq.connect('staffBotDb.db') as con:
        cur = con.cursor()

    cur.execute(f'SELECT users.timeEnter_mode FROM users WHERE telegram_id = {telID}')
    mode = cur.fetchone()[0]
    con.commit()
    return mode


def get_enter_time(telID: int):
    with sq.connect('staffBotDb.db') as con:
        cur = con.cursor()

    cur.execute(f'SELECT users.enter_time FROM users WHERE telegram_id = {telID}')
    time = cur.fetchone()[0]
    con.commit()
    return time


def set_enter_time(telID: int, time: str):
    with sq.connect('staffBotDb.db') as con:
        cur = con.cursor()

    cur.execute("UPDATE users SET enter_time = ? WHERE telegram_id = ?", (time, telID))
    con.commit()
