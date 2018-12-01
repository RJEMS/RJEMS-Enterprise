# Imports
import json
from flask import Flask
from flask import render_template, request, g, redirect, url_for
from flask_migrate import Migrate
from flask_oidc import OpenIDConnect
from okta import UsersClient
from models.models import *
from commands import *
from utils import *


migrate = Migrate(app, db)

LOGGED_IN_USER_EMAIL = "chauhan.shree@gmail.com"
LOGGED_IN_USER_NAME = "Rajshree"


app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = "yfrhkjdvknkjxhvbxhjfdgkdfjgk"
oidc = OpenIDConnect(app)

okta_client = UsersClient("https://dev-890723.oktapreview.com", "00vNpeJlZnNkz9QSN5wZN0Wzg02MsOfL_J4GazevFC")


@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
    else:
        g.user = None


# setting the route for the project
# rendering the home page


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/profile")
@oidc.require_login
def profile():
    user_details = get_logged_in_user_details(g)
    return render_template("profile.html", user=user_details)


@app.route("/dashboard")
@oidc.require_login
def dashboard():
    uploaded_files = get_uploaded_files()
    return render_template("dashboard.html", uploads=uploaded_files)


@app.route("/search", methods=['GET', 'POST'])
@oidc.require_login
def search():
    if request.method == 'POST':
        first_name = request.form['inputFirstName']
        last_name = request.form['inputLastName']
        users = get_users_by_filter(first_name, last_name)
        return render_template("search.html", users=users)
    users = get_all_users()
    return render_template("search.html", users=users)


@app.route("/upload")
@oidc.require_login
def upload():
    return render_template("upload.html")


@app.route("/login")
@oidc.require_login
def login():
    return redirect(url_for(".profile"))


@app.route("/logout")
def logout():
    oidc.logout()
    return redirect(url_for(".index"))


@app.route('/SearchUsingParams', methods=['POST'])
@oidc.require_login
def search_using_params():
    first_name = request.form['input_first_name']
    last_name = request.form['input_last_name']
    users = get_all_users(first_name, last_name)
    return render_template("search.html", users=users)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == "__main__":
    app.run()
