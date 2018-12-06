from application import app, db
from models.models import *
import datetime
from sqlalchemy import desc
from sqlalchemy import func, and_


# get logged in user role
def get_logged_in_user_role(g):
    user = User.query.filter_by(email=g.user.profile.email).first()
    if user is None:
        user = add_new_user(g)

    role_name = Role.query.filter_by(id=user.role_id).first().role_name
    return role_name


# get details of logged in user.
def get_logged_in_user_details(g):
    user = User.query.filter_by(email=g.user.profile.email).first()
    return user


# add a user to rjems db when user logs in first time.
def add_new_user(g):
    role_id = Role.query.filter_by(role_name="employee").first().id
    user = User(g.user.profile.firstName, g.user.profile.lastName, g.user.profile.email, role_id, 200000)
    db.session.add(user)
    db.session.commit()
    user = User.query.filter_by(email=g.user.profile.email).first()
    return user


# edit details of an existing user.
def edit_existing_user(form_data):
    user = User.query.filter_by(email=form_data['input_email']).first()
    user.phone = form_data['input_phone']
    user.bio = form_data['input_bio']
    user.address_line1 = form_data['input_address_line1']
    user.address_line2 = form_data['input_address_line2']
    user.city = form_data['input_city']
    user.state = form_data['input_state']
    db.session.commit()


# change role of an employee to manager.
def change_manager_role(email):
    role_id = Role.query.filter_by(role_name="manager").first().id
    user = User.query.filter_by(email=email).first()
    user.role_id = role_id
    db.session.commit()


# get all the users registered with the application.
def get_all_users():
    users = User.query.all()
    for user in users:
        user.role_name = Role.query.filter_by(id=user.role_id).first().role_name
    return users


# get users based on given filter.
def get_users_by_filter(first_name, last_name):
    search_query = User.query
    if first_name:
        search_query = search_query.filter(User.first_name.like('%{0}%'.format(first_name)))
    if last_name:
        search_query = search_query.filter(User.last_name.like('%{0}%'.format(last_name)))
    users = search_query.all()

    for user in users:
        user.role_name = Role.query.filter_by(id=user.role_id).first().role_name
    return users


# get all the images, training materials and text updates uploaded to the database.
def get_uploaded_files():
    uploaded_files = Upload.query.order_by(desc(Upload.id))
    return uploaded_files


# add a new image, training material or text update to database
def add_new_file(ext, name, file_path, text):
    upload = Upload(ext, file_path, name, text, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    db.session.add(upload)
    db.session.commit()
    return "successful"









