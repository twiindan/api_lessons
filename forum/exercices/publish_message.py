import requests
from nose.tools import assert_equals
import ujson


#MAKE A REQUEST TO PUBLISH A MESSAGE TO THE FORUM
'''
The URL is https://api-testing-conference.herokuapp.com/v1.0/forum
THE BODY SHOULD HAVE THE FOLLOWING MANDATORY PARAMETERS: theme, subject and message
THE THEME SHOULD BE ONE OF THE FOLLOWING OPTIONS:
FORUM_THEMES = Security, Development, Automation, Testing
ASSERT THE STATUS CODE (200) and the response content (message created)
MAKE A GET REQUEST TO OBTAIN ALL THE MESSAGES PUBLISHED IN THE FORUM
'''

requests.get('https://api-testing-conference.herokuapp.com/v1.0/reset')

url = 'https://api-testing-conference.herokuapp.com/v1.0/forum'

#DEFINE THE BODY IN A DICTIONARY WITH THE PARAMETERS REQUIRED



#CONVERT THE PYTHON DICTIONARY IN JSON WITH ujson.dumps



#SEND THE POST REQUEST



#ASSERT THE STATUS CODE



#ASSERT THE RESPONSE TEXT



#SEND A REQUEST TO OBTAIN ALL THE MESSAGES FROM THE FORUM



#ASSERT THE STATUS CODE



#CONVERT THE RESPONSE CONTENT TO JSON



#ASSERT THE MESSAGE

