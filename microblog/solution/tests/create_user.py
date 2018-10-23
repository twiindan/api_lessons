from nose.tools import assert_equals, assert_true, assert_is_not_none
from solution.core.microblog_api import MicroblogApi
from solution.model.User import User
from random import randint


class TestCreateUser():

    @classmethod
    def setup_class(self):
        self.microblog = MicroblogApi()

    def test_create_user(self):
        random_number = randint(1, 10000000)
        username = "User{}".format(random_number)
        email = "email{}@test.com".format(random_number)
        user = User(username=username, password='Testing83', email=email)
        response = self.microblog.create_user(body=user.to_dict())
        assert_equals(201, response.status_code)

    def test_create_user_without_username(self):
        random_number = randint(1, 10000000)
        email = "email{}@test.com".format(random_number)
        user = User(username=None, password='Testing83', email=email)
        response = self.microblog.create_user(body=user.to_dict())
        assert_equals(400, response.status_code)

    def test_create_user_without_email(self):
        random_number = randint(1, 10000000)
        username = "User{}".format(random_number)
        user = User(username=username, password='Testing83', email=None)
        response = self.microblog.create_user(body=user.to_dict())
        assert_equals(400, response.status_code)

    def test_create_existing_user(self):
        user = User(username='twiindan', password='Testing83', email='twiindan@gmail.com')
        response = self.microblog.create_user(body=user.to_dict())
        assert_equals(400, response.status_code)
