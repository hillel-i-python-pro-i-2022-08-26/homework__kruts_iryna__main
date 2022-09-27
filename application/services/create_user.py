import sqlite3

from faker import Faker

from homework__kruts_iryna__main.application.services import create_bd

fake = Faker()

def create_new_user():
    with sqlite3.connect('phones1.sqlite') as bd_con:
        cur = bd_con.cursor()
        cur.execute("""
            INSERT INTO phones(phone, contact_name, phone_value)
            VALUES(:phone, :contact_name, :phone_value)
        """, (88, fake.name(), 3000222)
        )
        cur.execute("SELECT * FROM phones")
        f = cur.fetchall()
    return f

def delete_user():



print(create_new_user())


