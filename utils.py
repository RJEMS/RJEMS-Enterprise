from application import app, db
from models.models import *
import datetime
from sqlalchemy import desc
from sqlalchemy import func, and_


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
    user.address_line1 = form_data['input_address_line1']
    user.address_line2 = form_data['input_address_line2']
    user.city = form_data['input_city']
    user.state = form_data['input_state']
    db.session.commit()


def change_manager_role(email):
    role_id = Role.query.filter_by(role_name="manager").first().id
    user = User.query.filter_by(email=email).first()
    user.role_id = role_id
    db.session.commit()


def get_payslip_data(email_id):
    return ""


def get_all_users():
    users = User.query.all()
    for user in users:
        user.role_name = Role.query.filter_by(id=user.role_id).first().role_name
    return users


def get_users_by_filter(first_name, last_name):
    if first_name != "" and last_name != "":
        users = User.query.filter_by(first_name=first_name, last_name=last_name)
        # users = User.query.filter(and_(func.lower(User.first_name) == func.lower(first_name),
        #                               func.lower(User.last_name) == func.lower(last_name))).first()

    if first_name != "" and last_name == "":
        users = User.query.filter_by(first_name=first_name)
    if first_name == "" and last_name != "":
        users = User.query.filter_by(last_name=last_name)
    if first_name == "" and last_name == "":
        users = User.query.all()

    for user in users:
        user.role_name = Role.query.filter_by(id=user.role_id).first().role_name
        print(user.role_name)
    return users


def get_uploaded_files():
    uploaded_files = Upload.query.order_by(desc(Upload.id))
    return uploaded_files


def add_new_file(ext, name, file_path, text):
    upload = Upload(ext, file_path, name, text, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    db.session.add(upload)
    db.session.commit()
    return "successful"









