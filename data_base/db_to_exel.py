import pandas as pd
import sqlite3 as sq

def create_report_to_xlsx():
    with sq.connect('staffBotDb.db') as con:
        cur = con.cursor()
    df = pd.read_sql('SELECT * FROM history', con)
    df.to_excel('report.xlsx', index=False)

    con.commit()
