from nose.tools import assert_equals, assert_true, assert_is_not_none
from solution.core.microblog_api import MicroblogApi


class TestGetUserInformation():

    @classmethod
    def setup_class(self):
        self.microblog = MicroblogApi()

    def get_token(self):
        username = 'twiindan'
        password = 'Testing83'
        response = self.microblog.get_new_token(username=username, password=password)
        json_body = response.json()
        token = json_body['token']
        headers = {"Authorization": "Bearer {}".format(token)}
        return headers

    def test_get_user_information(self):
        headers = self.get_token()
        response = self.microblog.get_user_information(headers=headers, user_id=2)
        assert_true(response.ok)
        json_body = response.json()
        assert_equals(json_body['username'], 'twiindan')

