from nose.tools import assert_equals, assert_true, assert_is_not_none
from exercise.core.microblog_api import MicroblogApi


class TestToken(object):

    @classmethod
    def setup_class(self):
        self.microblog = MicroblogApi()

    def test_get_new_token(self):
        pass
        # MAKE A REQUEST USING MICROBLOG API (GET NEW TOKEN FUNCTION) PASSING AS PARAMETER USERNAME AND PASSWORD


        # CONVERT BODY TO JSON


        #ASSERT TOKEN IS NOT NONE



    def test_error_when_get_token_with_invalid_password(self):
        pass
        # MAKE A REQUEST USING MICROBLOG API (GET NEW TOKEN FUNCTION) PASSING AS PARAMETER USERNAME AND INCORRECT PASSWORD


        # ASSERT STATUS CODE IS 401

    def test_error_when_get_token_with_invalid_username(self):
        pass
        # MAKE A REQUEST USING MICROBLOG API (GET NEW TOKEN FUNCTION) PASSING AS PARAMETER INCORRECT USERNAME AND PASSWORD


        # ASSERT STATUS CODE IS 401

