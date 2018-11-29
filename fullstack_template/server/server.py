# Imports
import json

from flask import render_template, request
from flask_migrate import Migrate

from application import app, db
from models.models import *
from commands import *


migrate = Migrate(app, db)

LOGGED_IN_USER_EMAIL = "chauhan.shree@gmail.com"
LOGGED_IN_USER_NAME = "Rajshree"

@app.route("/Index")
def index():
    # for successful login from okta/google
    successful_login = "Yes"
    if successful_login == "Yes":
        # check if user details exist in our db
        userdetails = getuserdetails(LOGGED_IN_USER_EMAIL, LOGGED_IN_USER_NAME)
        return render_template("index.html", text="successful")
    else:
        userdetails = ''
        return render_template("index.html", text="unauthorized")


def getuserdetails(email, name):
    user = User.query.filter_by(email=email).first()
    if user is None:
        newuser = addnewuser(email, name)
        return newuser
    else:
        return user


def addnewuser(email, name):
    return "true"


@app.route("/helloworld")
def helloworld():
    data = {"user": "Rajshree"}
    return json.dumps(data), 200, {"Content-Type": "application/json"}


if __name__ == "__main__":
    app.run()
