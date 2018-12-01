from application import app, db
from models.models import *

# constants
ADMIN_ROLE_STRING = 'manager' #'admin'  # 'employee'
ADMIN_USER_EMAIL = 'admin@rjems.com'

@app.cli.command()
def initdatabase():
    """Initializes database for first use.
    Creates an admin role and admin user."""
    # create_role()
    # create_admin_user()
    # create_uploads()


# def create_admin_user():
#     admin_user = User.query.filter_by(email=ADMIN_USER_EMAIL).first()
#     if admin_user is None:
#         role = Role.query.filter_by(role_name=ADMIN_ROLE_STRING).first()
#         if role is not None:
#             user = User('admin', ADMIN_USER_EMAIL, '123', role.id)
#             db.session.add(user)
#             db.session.commit()
#             print("created admin user {}".format(user))
#         else:
#             # TODO - logger.error this instead
#             print("Not creating user. create role first")
#     else:
#         print("admin user already exists")


def create_role():
    roles = Role.query.all()

    # TODO replace with python logger
    print("creating initial role")
    admin_role = Role(ADMIN_ROLE_STRING)
    db.session.add(admin_role)
    db.session.commit()
    roles = Role.query.all()
    print(roles)


def create_uploads():

    # TODO replace with python logger
    print("creating uploads role")
    uploads = Upload("Image", "dog", "")
    db.session.add(uploads)
    db.session.commit()
    uploaded = Upload.query.all()
    print(uploaded)






