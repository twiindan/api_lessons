__author__ = 'arobres'

import logging
import requests
from json import JSONEncoder
from solution.core.configuration import FORUM_HOSTNAME, HEADERS

POST = 'post'
GET = 'get'
DELETE = 'delete'
PUT = 'put'

#DEFINE THE ROUTES (TOKEN, USERS, USER_INFO...)
SERVER_ROOT = 'https://{}'.format(FORUM_HOSTNAME)


class MicroblogApi(object):

    def __init__(self):
        """Initialization method
        """

        self.api_url = SERVER_ROOT
        print("Initialized API REST Utils")

        self.encoder = JSONEncoder()
        self.initialize_logging()

    def initialize_logging(self):
        self.logger = logging.getLogger('forum')
        hdlr = logging.FileHandler('forum_testing.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        hdlr.setFormatter(formatter)
        self.logger.addHandler(hdlr)
        self.logger.setLevel(logging.DEBUG)

    def _call_api(self, pattern, method, body=None, headers=HEADERS, payload=None, auth=None, **kwargs):

        """Launch HTTP request to Policy Manager API with given arguments
        :param pattern: string pattern of API url with keyword arguments (format string syntax)
        :param method: HTTP method to execute (string)
        :param body: JSON body content (dict)
        :param headers: HTTP header request (dict)
        :param payload: Query parameters for the URL
        :param **kwargs: URL parameters (without url_root) to fill the patters
        :returns: REST API response
        """

        kwargs['url_root'] = self.api_url

        url = pattern.format(**kwargs)
        self.logger.info('NEW REQUEST TO SEND')
        self.logger.info('\nMETHOD: {}\nURL: {} \nHEADERS: {} \nBODY: {}'.format(method, url, headers,
                                                                                 self.encoder.encode(body)))
        if isinstance(body, dict):
            body = self.encoder.encode(body)

        try:
            r = requests.request(method=method, url=url, data=body, headers=headers,
                                 params=payload, auth=auth)

        except Exception as e:
            print("Request {} to {} crashed: {}".format(method, url, str(e)))
            return None

        return r

    def get_new_token(self, username=None, password=None):
        pass
        # CREATE THE AUTHENTICATION WITH USERNAME AND PASSWORD USING A TUPLA

        #CALL TO API WITH PATTERN, METHOD POST AND AUTHENTICATION



    def revoke_token(self, headers=None):
        pass
        #CALL TO API WITH PATTERN, METHOD DELETE AND HEADER WITH AUTHENTICATION



    def get_user_list(self, headers=None):
        pass
        #CALL TO API WITH PATTERN, METHOD GET AND HEADER WITH AUTHENTICATION



    def create_user(self, body=None):
        pass
        #CALL TO API WITH PATTERN, METHOD POST AND BODY TO CREATE USER



    def get_user_information(self, headers=None, user_id=None):
        pass
        # CALL TO API WITH PATTERN, METHOD GET AND HEADER WITH AUTHENTICATION (USER ID SHOULD BE IN URL PATH)
