from application import app, db
from models.models import *


def get_logged_in_user_details(g):
    user = User.query.filter_by(email=g.user.profile.email).first()
    if user is None:
        new_user = add_new_user(g)
        return new_user
    else:
        return user


def add_new_user(g):
    role_id = Role.query.filter_by(role_name="employee").first().id
    user = User(g.user.profile.firstName, g.user.profile.lastName, g.user.profile.email, '', '', role_id)
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(email=g.user.profile.email).first()
    return user


def edit_existing_user(form_data):
    user = User.query.filter_by(email=form_data['input_email']).first()
    user.phone = form_data['input_phone']
    user.bio = form_data['input_bio']
    db.session.commit()


def assign_manager_role(form_data):
    role_id = Role.query.filter_by(role_name="employee").first().id
    user = User.query.filter_by(email=form_data['input_email']).first()
    user.role_id = role_id
    db.session.commit()


def get_payslip_data(email_id):
    return ""



def get_all_users():
    users = User.query.all()
    return users


def get_users_by_filter(first_name, last_name):
    if first_name != "" and last_name != "":
        users = User.query.filter_by(first_name=first_name, last_name=last_name)
    if first_name != "" and last_name == "":
        users = User.query.filter_by(first_name=first_name)
    if first_name == "" and last_name != "":
        users = User.query.filter_by(last_name=last_name)
    if first_name == "" and last_name == "":
        users = User.query.all()
    return users


def get_uploaded_files():
    uploaded_files = Upload.query.limit(15).all()
    print(uploaded_files)
    return uploaded_files


def add_new_file():
    return ""









