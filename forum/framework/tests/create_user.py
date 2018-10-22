from nose.tools import assert_equals, assert_true
from framework.core.forum_api import ForumApi
from framework.model.user import User


class TestCreateMessage():

    @classmethod
    def setup_class(self):
        self.forum_api = ForumApi()
        self.forum_api.reset_mock()

    def test_create_user_with_all_parameters(self):
        pass
        #Create User instance with correct parameters

        #User create user function from self.forum_api to send the request create user


        #assert response is ok


        #assert response text is 'user created'

    def test_create_user_with_none_values(self):
        pass
        # Create User instance with correct parameters and name=None


        # User create user function from self.forum_api to send the request create user


        # assert response is ok


        # assert response text is 'user created'


    def test_create_user_invalid_json_format(self):

        body = 'hello, is not a JSON'

        # User create user function from self.forum_api to send the request to create user passing the incorrect body


        # assert response status code is 400


        #assert body has the key 'message' with value The JSON format is not correct



    def test_not_existent_role(self):
        pass
        # Create User instance with correct parameters but role = 'Not valid'


        # User create user function from self.forum_api to send the request create user


        # assert response status code is 400


        # assert body has the key 'message' with value 'Role not valid'



    def test_existent_user(self):
        pass
        # Create User instance with the same parameters first test


        # User create user function from self.forum_api to send the request create user


        # assert response status code is 409


        # assert body has the key 'message' with value 'User exist!'

