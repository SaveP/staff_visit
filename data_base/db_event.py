import sqlite3 as sq
import time

with sq.connect("staffBotDb.db") as con:
    cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS events(
                id_event	INTEGER UNIQUE,
                time    	TEXT,
                type    	TEXT,
                user_id 	INTEGER,
                id_chat 	INTEGER,
                id_msg_chat	INTEGER,
                id_grup 	INTEGER,
                id_msg_grup	INTEGER,
                description	TEXT,
                links   	TEXT,
                user_nick	TEXT,
                PRIMARY KEY(id_event AUTOINCREMENT)
                )""")

con.commit()

def add_event(user_id: int, id_chat: int = None, id_msg_chat: int = None, id_grup: int = None, id_msg_grup: int = None,
              description: str = "", links: str = "", user_nick: str = "", type: str = ""):
    with sq.connect("staffBotDb.db") as con:
        cur = con.cursor()

    named_tuple = time.localtime()  # получить struct_time
    local_time = time.strftime("%H:%M %d/%m/%Y", named_tuple)

    cur.execute("""INSERT INTO events (time, type, user_id, id_chat, id_msg_chat, id_grup, id_msg_grup, description, 
    links, user_nick) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (local_time, type, user_id, id_chat, id_msg_chat, id_grup, id_msg_grup, description, links, user_nick))

    id_event = cur.lastrowid

    con.commit()

    return id_event


def find_event(id_chat, id_msg):
    with sq.connect("staffBotDb.db") as con:
        cur = con.cursor()
        cur.row_factory = sq.Row
        cur.execute(f'SELECT * FROM events WHERE id_chat = ? AND id_msg_chat = ? ORDER BY RANDOM() LIMIT 1',
                    (id_chat, id_msg))
        data = dict(cur.fetchone())
        con.commit()
        return data
