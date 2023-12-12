import sqlite3 as sq

with sq.connect("staffBotDb.db") as con:
    cur = con.cursor()

cur.execute('ALTER TABLE users ADD COLUMN enter_time TEXT')

con.commit()
