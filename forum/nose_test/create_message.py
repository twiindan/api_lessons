import ujson

import requests

__author__ = 'arobres'

from nose.tools import assert_equals, assert_true


class TestCreateMessage():

    forum_url = 'https://api-testing-conference.herokuapp.com/v1.0/forum'

    def test_create_message_with_all_parameters(self):

        body = {'theme': 'Testing', 'subject': 'Using nosetests', 'message': "I'm doing a framework!"}
        body = ujson.dumps(body)
        response = requests.post(url=self.forum_url, data=body)
        assert_true(response.ok)
        assert_equals(response.text, 'message created')

    def test_create_message_with_none_parameters(self):

        body = {'theme': None, 'subject': None, 'message': None}
        body = ujson.dumps(body)

        response = requests.post(url=self.forum_url, data=body)
        assert_equals(response.status_code, 400)
        response_json = response.json()
        assert_equals(response_json['message'], 'Theme not valid')

    def test_create_message_with_incorrect_json_format(self):

        body = 'Not JSON format'
        response = requests.post(url=self.forum_url, data=body)
        assert_equals(response.status_code, 400)
        response_json = response.json()
        assert_equals(response_json['message'], 'The JSON format is not correct')


    def test_create_message_with_incorrect_theme(self):

        body = {'theme': 'Not Valid', 'subject': 'Using nosetests', 'message': "I'm doing a framework!"}
        body = ujson.dumps(body)
        response = requests.post(url=self.forum_url, data=body)
        assert_equals(response.status_code, 400)
        response_json = response.json()
        assert_equals(response_json['message'], 'Theme not valid')



