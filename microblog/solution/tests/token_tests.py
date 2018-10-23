from nose.tools import assert_equals, assert_true, assert_is_not_none
from solution.core.microblog_api import MicroblogApi


class TestCreateMessage():

    @classmethod
    def setup_class(self):
        self.forum_api = MicroblogApi()

    def test_get_new_token(self):

        username = 'twiindan'
        password = 'Testing83'
        response = self.forum_api.get_new_token(username=username, password=password)
        json_body = response.json()
        token = json_body['token']
        assert_is_not_none(token)

    def test_error_when_get_token_with_invalid_password(self):
        username = 'twiindan'
        password = 'Testing'
        response = self.forum_api.get_new_token(username=username, password=password)
        assert_equals(401, response.status_code)

    def test_error_when_get_token_with_invalid_username(self):
        username = 'notvalid'
        password = 'Testing83'
        response = self.forum_api.get_new_token(username=username, password=password)
        assert_equals(401, response.status_code)

    def test_revoke_token_with_valid_token(self):
        username = 'twiindan'
        password = 'Testing83'
        response = self.forum_api.get_new_token(username=username, password=password)
        json_body = response.json()
        token = json_body['token']
        headers = {"Authorization": "Bearer {}".format(token)}
        response = self.forum_api.revoke_token(headers)
        assert_true(response.ok)

    def test_revoke_token_with_invalid_token(self):
        headers = {"Authorization": "Bearer {}".format('not valid token')}
        response = self.forum_api.revoke_token(headers)
        assert_equals(401, response.status_code)

    def test_revoke_token_without_token(self):
        response = self.forum_api.revoke_token()
        assert_equals(401, response.status_code)