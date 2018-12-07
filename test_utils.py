from utils import *
from models import models
import json, warnings, unittest, string, random


# Disabling warning messages when running unit test
def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", 'ResourceWarning')
            test_func(self, *args, **kwargs)
    return do_test



# Unit test for Utils class
class Testing(unittest.TestCase):

    # Checks to see if there are uploaded files
    def test_get_uploaded_files(self):
        files = get_uploaded_files().all()
        count = len(files)
        assert count != 0
        upload = Upload('gif', '/static/uploads/giphy.gif', 'giphy.gif', '', '2018-12-04 01:38:04')
        upload.id = 2
        assert upload in files

    # Checks to see if file is added succesfully
    def test_add_new_file(self):
        assert (add_new_file('text', 'TEST', '/static/uploads/', 'teststsljlkljdlfsdklfdls')) == 'successful'

    # Retrieve the user list and checks if there that many users
    def test_get_all_users(self):
        users = get_all_users()
        assert len(users) == 4

    # Gets a user by first and last name and checks if they contain the right info
    def test_get_users_by_filter(self):
        users = get_users_by_filter('RJEMS', 'RJEMS')
        assert len(users) == 1
        assert users[0].first_name == 'RJEMS'
        assert users[0].last_name == 'RJEMS'
        assert users[0].phone == '222-333-4444'
        assert users[0].city == 'San Jose'


    #Changing role of a user and checking if its been changed
    def test_change_manager_role(self):
        change_manager_role("sindhujaramini@gmail.com")
        users = get_users_by_filter('Sindhuja', 'Ramini')
        assert users[0].role_name == 'manager'

if __name__ == '__main__':
    unittest.main()
