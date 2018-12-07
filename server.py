# Imports

from flask import render_template, request, g, redirect, url_for, session
from flask_migrate import Migrate
from flask_oidc import OpenIDConnect
from okta import UsersClient
import os
from werkzeug.utils import secure_filename
from models.models import *
from commands import *
from utils import *

migrate = Migrate(app, db)


app.config["OIDC_CLIENT_SECRETS"] = "client_secrets.json"
app.config["OIDC_COOKIE_SECURE"] = False
app.config["OIDC_CALLBACK_ROUTE"] = "/oidc/callback"
app.config["OIDC_SCOPES"] = ["openid", "email", "profile"]
app.config["SECRET_KEY"] = "yfrhkjdvknkjxhvbxhjfdgkdfjgk"
oidc = OpenIDConnect(app)

okta_client = UsersClient("https://dev-664783.oktapreview.com", "00pIz5wsJSahcbI1dp-czYIeocQdBw2ffUIYMjE7lP")

UPLOAD_FOLDER = './static/uploads'
RETRIEVE_FOLDER = '/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.before_request
def before_request():
    if oidc.user_loggedin:
        g.user = okta_client.get_user(oidc.user_getfield("sub"))
        session['role_name'] = get_logged_in_user_role(g)
    else:
        g.user = None


@app.route("/login")
@oidc.require_login
def login():
    return redirect(url_for(".profile"))


@app.route("/logout")
def logout():
    oidc.logout()
    return redirect(url_for(".index"))


@app.route('/')
def index():
    return render_template('index.html')


# renders the profile page if the user is logged in.
@app.route("/profile", methods=['GET', 'POST'])
@oidc.require_login
def profile():
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
              "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
              "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
              "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
              "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    if request.method == 'POST':
        edit_existing_user(request.form)
        user_details = get_logged_in_user_details(g)
        return render_template("profile.html", user=user_details, states=states, success='true')
    user_details = get_logged_in_user_details(g)
    return render_template("profile.html", user=user_details, states=states, success='false')


# renders the dashboard page if the user is logged in.
@app.route("/dashboard")
@oidc.require_login
def dashboard():
    uploaded_files = get_uploaded_files()
    return render_template("dashboard.html", uploads=uploaded_files)


# renders the search page if the user is logged in.
# handles search functionality in post method
@app.route("/search", methods=['GET', 'POST'])
@oidc.require_login
def search():
    if request.method == 'POST':
        first_name = request.form['input_first_name']
        last_name = request.form['input_last_name']
        users = get_users_by_filter(first_name, last_name)
        return render_template("search.html", users=users)
    users = get_all_users()
    return render_template("search.html", users=users)


# renders the upload page if the user is logged in.
# handles upload functionality in post method
@app.route("/upload", methods=['GET', 'POST'])
@oidc.require_login
def upload():
    if session['role_name'] != 'admin':
        return render_template("error.html")
    if request.method == 'POST':
        if 'file' not in request.files:
            text = request.form['input_upload_text']
            add_new_file('text', '', '', text)
            return render_template("upload.html", success='text_true')
        file = request.files['file']
        ext = file.filename.rsplit('.', 1)[1].lower()
        name = file.filename.rsplit('.', 0)[0]
        file_path = RETRIEVE_FOLDER + '/' + file.filename

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        add_new_file(ext, name, file_path, '')
        return render_template("upload.html", success='upload_true')
    else:
        return render_template("upload.html")


# change role of an employee to manager
@app.route('/assign_manager_role', methods=['POST'])
@oidc.require_login
def assign_manager_role():
    email = request.get_data().decode('utf-8')
    change_manager_role(email)
    users = get_all_users()
    return render_template("search.html", users=users)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, ssl_context=('cert.pem', 'key.pem'))
