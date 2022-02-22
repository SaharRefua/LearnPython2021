from flask import Flask

app = Flask(__name__)


@app.route("/")
def hellow():
    return "Hellow world!"


@app.route("/about")
def about():
    return "<h1>about page</h1>"


if True:
    app.run(debug=True)
