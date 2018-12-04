from application import db


class User(db.Model):
    """
    TODO : Add documentation
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.Integer())
    bio = db.Column(db.String(255))
    address_line1 = db.Column(db.String(255))
    address_line2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    state = db.Column(db.String(255))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, first_name, last_name, email, phone, bio, address_line1, address_line2, city, state, role_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.bio = bio
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.state = state
        self.role_id = role_id

    def __repr__(self):
        return '<id {}, name {}>'.format(self.id, self.first_name + ' ' + self.last_name)


class Salary(db.Model):
    """
    TODO : Add documentation
    """
    __tablename__ = 'salaries'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return '<id {}, user_id {}>'.format(self.id, self.user_id)


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


class Upload(db.Model):
    """
    TODO: Add documentation
    """
    __tablename__= 'uploads'

    id = db.Column(db.Integer, primary_key=True)
    upload_type = db.Column(db.String(255))
    url = db.Column(db.String(255))
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.String)

    def __init__(self, upload_type, url, title, text, date):
        self.upload_type = upload_type
        self.url = url
        self.title = title
        self.text = text
        self.date = date

    def __repr__(self):
        return '<id {}, upload_type {}, url {}, title {}, text {}, date{}>'.format(self.id, self.upload_type, self.url,
                                                                                   self.title, self.text, self.date)
