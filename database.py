import sqlite3
from datetime import *



class DB:
    def __init__(self) -> None:
        self.con = sqlite3.connect('clock.db')
        self.cur = self.con.cursor()


    def create_table(self):

        """
        CREATE TIME TABLE TO SAVE USER'S TIMES

        """
        self.cur.execute("CREATE TABLE IF NOT EXISTS time(id INTEGER PRIMARY KEY, user_time TEXT)")
        self.con.commit()


    def add_time_to_db(self, *time:str):

    
        for i in time:
            
            try:
                self.cur.execute("""INSERT INTO time(user_time) VALUES (?) """, (i, ))
                self.con.commit()

            except ValueError:

                ValueError('Type Eror: input %s must be whole numeric string' % i )
            

    def read_last_time(self):
        try:
            time = self.cur.execute('SELECT * FROM time WHERE ID = (SELECT MAX(ID) FROM time)')
            return time.fetchall()
        except RuntimeError:
            RuntimeError("error during gettig last records\n perhaps the time table is not yet created\n or there's no record")


    def get_all_records(self):
        try:
            times = self.cur.execute('SELECT * FROM time')
            return [i for i in times.fetchall()]

        except RuntimeError:
            RuntimeError("error during gettig all records\n perhaps the time table is not yet created\n or there's no record")


    def delete_all_records(self):
        
            self.cur.execute('DELETE FROM time')
            self.con.commit()
        

