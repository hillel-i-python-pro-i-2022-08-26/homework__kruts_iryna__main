import sqlite3

from flask import Flask, render_template
# from application.services import bd_creator
from application.services import create_new_user
from homework__kruts_iryna__main.application.services import create_bd

app = Flask("My site")


@app.route("/")
def hello():
    return "Hello, world!"


@app.route("/show-all/")
def show_some_from_bd():
    pass
    # result = bd_creator()
    # return render_template("show_all.html", result=result, title="showall")


@app.route("/create-user/")
def new_users():
    create_bd.bd_creator()
    list_of_users = create_new_user()
    return render_template('create_user.html', list_of_users=list_of_users, title='list_of_users')


@app.route('/create-user/int:<user_id>')
def delete_user(user_id):
    with sqlite3.connect('phones1.sqlite') as bd:
        cur = bd.cursor()
        cur.execute(f"DELETE FROM phones WHERE phone {user_id}")
        res = cur.fetchall()
    return f"Deleted phone with id {user_id}. The rest is {res}"


if __name__ == "__main__":
    app.run()
