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

        # CREATE USER BODY USING THE USER OBJECT

        # SEND REQUEST TO CREATE NEW USER PASSING AS PARAMETER THE BODY AS DICT

        # ASSERT STATUS CODE IS 201


    def test_create_existing_user(self):
        pass
        # CREATE USER (USING MODEL) WITH EXISTANT USER


        # SEND REQUEST TO CREATE NEW USER PASSING AS PARAMETER THE BODY AS DICT


        # ASSERT STATUS CODE IS 400

