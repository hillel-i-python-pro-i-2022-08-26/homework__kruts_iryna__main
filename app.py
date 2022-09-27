import sqlite3

from flask import Flask, render_template
#from application.services import bd_creator
from application.services import create_new_user
from homework__kruts_iryna__main.application.services import create_bd

app = Flask("My site")


@app.route("/")
def hello():
    return "Hello, world!"


@app.route("/show-all/")
def show_some_from_bd():
    pass
    #result = bd_creator()
    #return render_template("show_all.html", result=result, title="showall")


@app.route("/create-user/")
def new_users():
    create_bd.bd_creator()
    res = create_new_user()
    print(type(res))
    return f'{res}'

@app.route('/create-user/int:<id>')
def delete_user(id):
    with sqlite3.connect('phones1.sqlite') as bd:
        cur = bd.cursor()
        cur.execute(f"DELETE FROM phones WHERE phone {id}")
        res = cur.fetchall()
    return f"Deleted phone with id {id}. The rest is {res}"



if __name__ == "__main__":
    app.run()
