# Code by Emmeline
from utils import add_new_user
import json, warnings, unittest, string, random
from contextlib import contextmanager
from flask import appcontext_pushed, g, json, jsonify
import flask

app = flask.Flask(__name__)

# Disabling warning messages when running unit test
def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", 'ResourceWarning')
            test_func(self, *args, **kwargs)
    return do_test


@contextmanager
def user_set(app, user):
    def handler(sender, **kwargs):
        g.user = user
    with appcontext_pushed.connected_to(handler, app):
        yield


# Unit tests for oauth_req and oauth_post methods
class Testing(unittest.TestCase):


    # Test valid GET request using oauth_req
    @ignore_warnings
    def test_add_new_user(self):
        with app.test_request_context('/?role_name=employee?Name=Peter'):
            res = add_new_user(g)
            print (res)
            #json_data = json.loads(res)
            #assert json_data

    #@app.route('/users/me')
    #def users_me():
    #    return jsonify(username=g.user.username)




if __name__ == '__main__':
    unittest.main()
