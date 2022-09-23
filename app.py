from random import random

from faker import Faker
from flask import Flask, render_template

from generate_json import generate_json
from generate_users import generate_list_of_person
from read_csv import calculate_csv

app = Flask("My first site")
fake = Faker()


@app.route("/")
def hello():
    return "Hello, world!"


@app.route("/requirements/")
def return_poem():
    with open("poem.txt", "r") as reader:
        result = reader.readlines()
        return render_template("requirements.html", result=result, title="requirements")


@app.route("/generate_users/")
def generate_users():
    new_gen = generate_list_of_person(random.randint(1, 100))
    return render_template("generate_users.html", new_gen=new_gen, title="generate_users")


@app.route("/space/")
def amt_astronauts():
    result = generate_json("http://api.open-notify.org/astros.json")
    return render_template("space.html", result=result, len=len, title="space")


@app.route("/mean/")
def read_csv():
    return f"<h1>{calculate_csv()}</h11>"


if __name__ == "__main__":
    app.run()
