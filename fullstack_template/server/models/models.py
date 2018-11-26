from application import db


class User(db.Model):
    """
    TODO : Add documentation
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.Integer())
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, name, email, phone, role_id):
        self.name = name
        self.email = email
        self.phone = phone
        self.role_id = role_id

    def __repr__(self):
        return '<id {}, name {}>'.format(self.id, self.name)


class Role(db.Model):
    """
    TODO: Add documentation
    """
    __tablename__= 'roles'

    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(255))

    def __init__(self, role_name):
        self.role_name = role_name

    def __repr__(self):
        return '<id {}, role_name {}>'.format(self.id, self.role_name)
