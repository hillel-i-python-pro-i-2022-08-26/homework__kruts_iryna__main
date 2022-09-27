import sqlite3
from typing import List

def bd_creator() -> None:
    """
    Функция для создания и минимальной работы с БД
    :return: данные из БД [[значение где phone_value>200], первое значение]
    """
    with sqlite3.connect("phones1.sqlite") as bd_connection:
        cursor = bd_connection.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS phones(
                 phone INTEGER PRIMARY KEY AUTOINCREMENT,
                 contact_name TEXT,
                 phone_value INTEGER
            )
        """
        )
    return None
