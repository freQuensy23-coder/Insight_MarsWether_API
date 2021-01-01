import sqlite3


class DB:
    def __init__(self, file_name = "data.sqlite"):
        self.file_name = file_name
        self.connection = sqlite3.connect(database="data.sqlite")
        # TODO Logging

    def add_new_day_info(self, info, day):
        cur = self.connection.cursor()
        q = f"""INSERT into days_info (day, information) VALUES ({day}, '{info}')"""
        cur.execute(q)
        self.connection.commit()

    def get_day_info(self, day: int)-> str:
        cur = self.connection.cursor()
        q = f"""SELECT * FROM days_info WHERE day = {day}"""
        cur.execute(q)
        res = cur.fetchone()
        return res

    def get_days_info(self, day_start, day_end):
        cur = self.connection.cursor()
        q = f"""SELECT * FROM days_info WHERE day >= {day_start} AND day <= {day_end}"""
        cur.execute(q)
        res = cur.fetchall()
        return res
