import sqlite3

from faker import Faker

from homework__kruts_iryna__main.application.services import create_bd

fake = Faker()

def create_new_user():
    with sqlite3.connect('phones1.sqlite') as bd_con:
        cur = bd_con.cursor()
        cur.execute("""
            INSERT INTO phones(contact_name, phone_value)
            VALUES(:contact_name, :phone_value)
        """, (fake.name(), 3000222)
        )
        cur.execute("SELECT * FROM phones")
        f = cur.fetchall()
    return f

print(create_new_user())


