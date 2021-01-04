import sqlite3
import logging
import time

logger = logging.getLogger("db_logger")


class DB:
    def __init__(self, file_name="data.sqlite"):
        self.file_name = file_name
        self.connection = sqlite3.connect(database="data.sqlite")
        # TODO Logging

    def add_new_day_info(self, info: str, day: int):
        with sqlite3.connect(self.file_name) as con:
            cur = con.cursor()
            info = info.replace("'", '"')
            q = f"""INSERT into days_info (day, information, creation_time) VALUES ({day}, '{info}, {time.time()}')"""
            logger.debug(f"Add new day info. q = {q}`")
            cur.execute(q)
            self.connection.commit()

    def get_day_info(self, day: int) -> str:
        with sqlite3.connect(self.file_name) as con:
            cur = con.cursor()
            q = f"""SELECT * FROM days_info WHERE day = {day}"""
            cur.execute(q)
            res = cur.fetchone()
            return res

    def get_days_info(self, day_start, day_end):
        with sqlite3.connect(self.file_name) as con:
            cur = con.cursor()
            q = f"""SELECT * FROM days_info WHERE day >= {day_start} AND day <= {day_end}"""
            cur.execute(q)
            res = cur.fetchall()
            return res
