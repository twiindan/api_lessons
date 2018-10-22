from nose.tools import assert_equals, assert_true
from framework.core.forum_api import ForumApi
from framework.model.user import User


class TestCreateMessage():

    @classmethod
    def setup_class(self):
        self.forum_api = ForumApi()
        self.forum_api.reset_mock()

    def test_create_user_with_all_parameters(self):
        body = User(name='Testing1234', username='Testing1234', password='testing', email='testing1234@testing1234.es',
                    role='QA')
        response = self.forum_api.create_user(body=body.to_dict())
        assert_true(response.ok)
        assert_equals(response.text, 'user created')

    def test_create_user_with_none_values(self):
        body = User(name=None, username='hello', password='easypwd', email='arobres@arobres.es', role='QA')
        response = self.forum_api.create_user(body=body.to_dict())
        assert_true(response.ok)
        assert_equals(response.text, 'user created')

    def test_create_user_invalid_json_format(self):

        body = 'hello, is not a JSON'
        response = self.forum_api.create_user(body=body)
        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'The JSON format is not correct')

    def test_not_existent_role(self):
        body = User(name='Testing7890', username='Testing7890', password='testing', email='testing7890@testing7890.es',
                    role='Not valid')
        response = self.forum_api.create_user(body=body.to_dict())

        assert_equals(response.status_code, 400)
        response_body = response.json()
        assert_equals(response_body['message'], 'Role not valid')

    def test_existent_user(self):
        body = User(name='Testing1234', username='Testing1234', password='testing', email='testing1234@testing1234',
                    role='QA')
        response = self.forum_api.create_user(body=body.to_dict())
        assert_equals(response.status_code, 409)
        response_body = response.json()
        assert_equals(response_body['message'], 'User exist!')
