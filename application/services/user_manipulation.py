import sqlite3

from faker import Faker


fake = Faker()

def create_new_user():
    with sqlite3.connect('phones.sqlite') as bd_con:
        cur = bd_con.cursor()
        cur.execute("""
            INSERT INTO phones(ContactName, PhoneValue)
            VALUES(:ContactName, :PhoneValue)
        """, (fake.name(), 3000222)
        )
        cur.execute("SELECT * FROM phones")
        result = cur.fetchall()
    return result

def delete_user(user_id):
    with sqlite3.connect('phones.sqlite') as bd:
        cur = bd.cursor()
        cur.execute(f"DELETE FROM phones WHERE PhoneId = {user_id}")
        cur.execute("SELECT * FROM phones")
        result = cur.fetchall()
        return result

def update_user(user_name):
    with sqlite3.connect('phones.sqlite') as bd_conn:
        cursor = bd_conn.cursor()
        cursor.execute(f"UPDATE phones SET ContactName={user_name}")
        result = cursor.fetchall()
        return result
