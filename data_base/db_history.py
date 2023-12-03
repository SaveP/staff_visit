import sqlite3 as sq

with sq.connect("staffBotDb.db") as con:
    cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS history(
                telegram_id INTEGER,
                senderName TEXT,
                employee_name TEXT,
                direct TEXT,
                time TEXT
                )""")

con.commit()

def addEntry(telID: int, senderName: str, employee_name: str, dir: str, time: str):
    with sq.connect("staffBotDb.db") as con:
        cur = con.cursor()

    cur.execute("""INSERT INTO history (telegram_id, senderName, employee_name, direct, time)
                    VALUES(?, ?, ?, ?, ?)""", (telID, senderName, employee_name, dir, time))

    con.commit()
