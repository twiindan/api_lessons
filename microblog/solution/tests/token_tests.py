from nose.tools import assert_equals, assert_true, assert_is_not_none
from solution.core.microblog_api import MicroblogApi


class TestToken():

    @classmethod
    def setup_class(self):
        self.microblog = MicroblogApi()

    def test_get_new_token(self):

        username = 'twiindan'
        password = 'Testing83'
        response = self.microblog.get_new_token(username=username, password=password)
        json_body = response.json()
        token = json_body['token']
        assert_is_not_none(token)

    def test_error_when_get_token_with_invalid_password(self):
        username = 'twiindan'
        password = 'Testing'
        response = self.microblog.get_new_token(username=username, password=password)
        assert_equals(401, response.status_code)

    def test_error_when_get_token_with_invalid_username(self):
        username = 'notvalid'
        password = 'Testing83'
        response = self.microblog.get_new_token(username=username, password=password)
        assert_equals(401, response.status_code)

    def test_revoke_token_with_valid_token(self):
        username = 'twiindan'
        password = 'Testing83'
        response = self.microblog.get_new_token(username=username, password=password)
        json_body = response.json()
        token = json_body['token']
        headers = {"Authorization": "Bearer {}".format(token)}
        response = self.microblog.revoke_token(headers)
        assert_true(response.ok)

    def test_revoke_token_with_invalid_token(self):
        headers = {"Authorization": "Bearer {}".format('not valid token')}
        response = self.microblog.revoke_token(headers)
        assert_equals(401, response.status_code)

    def test_revoke_token_without_token(self):
        response = self.microblog.revoke_token()
        assert_equals(401, response.status_code)