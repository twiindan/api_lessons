from nose.tools import assert_equals, assert_true
from framework.core.forum_api import ForumApi
from framework.model.user import User


class TestCreateMessage():

    @classmethod
    def setup_class(self):
        self.forum_api = ForumApi()

    def test_create_user_with_all_parameters(self):
        body = User(name='Testing1234', username='Testing1234', password='testing', email='testing1234@testing1234',
                    role='QA')
        response = self.forum_api.create_user(body=body.to_dict())
        assert_true(response.ok)
        assert_equals(response.text, 'user created')

