from flask import Flask, render_template
from application.services import bd_creator

app = Flask("My site")


@app.route("/")
def hello():
    return "Hello, world!"


@app.route("/show-all/")
def show_some_from_bd():
    result = bd_creator()
    return render_template("show_all.html", result=result, title="showall")


if __name__ == "__main__":
    app.run()
