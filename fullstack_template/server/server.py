# Imports

from flask import render_template, request
from flask_migrate import Migrate

from application import app, db
from models.models import *
from commands import *


migrate = Migrate(app, db)



# @app.route('/', methods=['POST', 'GET'])
# def home():
# 	if request.method=='POST':
#    		username = request.form['username']
#    		password = request.form['password']
#    		dbHandler.insertUser(username, password)
#    		users = dbHandler.retrieveUsers()
# 		return render_template('login.html', users=users)
#    	else:
#    		return render_template('login.html')


@app.route("/Index")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run()
