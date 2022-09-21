import sqlite3
from datetime import *

class DB:
    def __init__(self) -> None:
        self.con = sqlite3.connect('clock.db')
        self.cur = self.con.cursor()


    def create_table(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS time(id INTEGER PRIMARY KEY, user_time TEXT)")
        self.con.commit()

    def add_time_to_db(self, *time):
        for i in time:
            self.cur.execute("""INSERT INTO time(user_time) VALUES (?) """, (i, ))
            

    def read_last_time(self):
        time = self.cur.execute('SELECT * FROM time WHERE ID = (SELECT MAX(ID) FROM time)')
        return time.fetchall()


    def get_all_records(self):
        times = self.cur.execute('SELECT * FROM time')
        return times.fetchall()


    def delete_all_records(self):
        self.cur.execute('DELETE FROM time')
        self.con.commit()

    