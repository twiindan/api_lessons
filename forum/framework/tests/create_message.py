from nose.tools import assert_equals, assert_true
from framework.model.forum_message import ForumMessage
from framework.core.forum_api import ForumApi


class TestCreateMessage():

    @classmethod
    def setup_class(self):
        self.forum_api = ForumApi()

    def test_create_message_with_all_parameters(self):

        body = ForumMessage(theme='Testing', subject='Using framework', message="I'm doing a framework!")
        response = self.forum_api.create_message_forum(body=body.to_dict())
        assert_true(response.ok)
        assert_equals(response.text, 'message created')

    def test_create_message_with_none_parameters(self):

        body = ForumMessage(theme=None, subject=None, message=None)
        response = self.forum_api.create_message_forum(body=body.to_dict())
        assert_equals(response.status_code, 400)
        response_json = response.json()
        assert_equals(response_json['message'], 'Theme not valid')

    def test_create_message_with_incorrect_json_format(self):

        body = 'Not JSON format'
        response = self.forum_api.create_message_forum(body=body)
        assert_equals(response.status_code, 400)
        response_json = response.json()
        assert_equals(response_json['message'], 'The JSON format is not correct')


    def test_create_message_with_incorrect_theme(self):

        body = ForumMessage(theme='Not Valid', subject='Using framework', message="I'm doing a framework!")
        response = self.forum_api.create_message_forum(body=body.to_dict())
        assert_equals(response.status_code, 400)
        response_json = response.json()
        assert_equals(response_json['message'], 'Theme not valid')
