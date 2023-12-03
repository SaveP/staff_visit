import sqlite3 as sq

# Подключаемся к базе данных для бота
with sq.connect("staffBotDb.db") as con:
    cur = con.cursor()

#cur.execute('DROP TABLE employees')

# Создаём таблицу со всеми сотрудниками которые будут пересекать кпп
cur.execute("""CREATE TABLE IF NOT EXISTS employees (
            person_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            view TEXT,
            telegram_id INTEGER)""")

con.commit()


def new_employee(person_id: int, name: str, view: str, telegram_id: int):
    try:
        with sq.connect("staffBotDb.db") as con:
            cur = con.cursor()

        sqlite_insert_with_param = "INSERT INTO employees (person_id, name, view, telegram_id) VALUES(?, ?, ?, ?)"
        data_tuple = (person_id, name, view, telegram_id)
        cur.execute(sqlite_insert_with_param, data_tuple)

        con.commit()

    except sq.Error as error:
        print("Ошибка при работе с SQLite", error)

    finally:
        if con:
            con.close()
            print("Соединение с SQLite закрыто")


'''for i in personalList.staff:
    new_employee(i['ID'], i['Name'], i['View'], i['Telegram_ID'])'''


def print_all_employees():
    with sq.connect("staffBotDb.db") as con:
        cur = con.cursor()

    a = cur.execute("SELECT * FROM employees").fetchall()
    print(a)

    con.commit()


def get_all_employees():
    with sq.connect("staffBotDb.db") as con:
        cur = con.cursor()

    a = cur.execute("SELECT * FROM employees").fetchall()
    con.commit()
    return a
