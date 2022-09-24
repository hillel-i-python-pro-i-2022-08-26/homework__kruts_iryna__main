import sqlite3
from typing import List, Tuple

from faker import Faker

fake = Faker()
item_list = [(1, f'{fake.name()}', 2), (2, fake.name(), 33), (3, f'{fake.name()}', 200), (4, fake.name(), 14),
             (5, f'{fake.name()}', 2), (6, fake.name(), 1222)]


def bd_creator() -> List:
    # -> List[List, Tuple]
    """
    Функция для создания и минимальной работы с БД
    :return: данные из БД [[значение где phone_value>200], первое значение]
    """
    with sqlite3.connect('phones.sqlite') as bd_connection:
        cursor = bd_connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS phones(
        phone INTEGER PRIMARY KEY AUTOINCREMENT,
        contact_name TEXT,
        phone_value INTEGER
        )
        """)
        cursor.executemany("""
           INSERT INTO
              phones(phone, contact_name, phone_value)
           VALUES
        (:phone, :contact_name, :phone_value)
    """, item_list)
        read_first_row = cursor.execute("SELECT * FROM phones")
        result_some = read_first_row.fetchone()
        cursor.execute("UPDATE phones SET phone_value=phone_value+500")
        read_all_bd = cursor.execute("SELECT * FROM phones WHERE phone_value > 100")
        result = read_all_bd.fetchall()
        cursor.execute("DELETE FROM phones WHERE phone IN(1,3)")
        cursor.execute("""
                DROP TABLE phones;
                """)
        return result

