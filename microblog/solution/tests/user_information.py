from nose.tools import assert_equals, assert_true
from solution.core.microblog_api import MicroblogApi
from solution.model.ModifyUser import ModifyUser


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

    def test_get_user_information_with_invalid_token(self):
        headers = {"Authorization": "Bearer {}".format('not valid')}
        response = self.microblog.get_user_information(headers=headers, user_id=2)
        assert_equals(401, response.status_code)

    def test_modify_profile(self):
        headers = self.get_token()
        headers['Content-Type'] = 'application/json'
        body = ModifyUser(username='twiindan', email='twiindan@gmail.com', about_me='API Expert')
        response = self.microblog.modify_user_information(headers=headers, user_id=2, body=body.to_dict())
        print(response.status_code)
        print(response.json())
        assert_true(response.ok)
        json_body = response.json()
        assert_equals(json_body['about_me'], 'API Expert')
