# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# configuration
app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

# TODO load this configuration from a cfg file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rjems.db'

db = SQLAlchemy(app)
