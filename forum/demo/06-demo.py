__author__ = 'arobres'
import requests

### CUSTOM HEADERS ###

headers = {'my_header': 'important_header', 'content-type': 'application/json'}
response = requests.get('https://api-testing-conference.herokuapp.com/v1.0', headers=headers)
print(response.request.headers)

### COOKIES ###

url = 'https://api-testing-conference.herokuapp.com/v1.0/welcome'
response = requests.get(url=url)
cookies = response.cookies
print(response.text)
response = requests.get(url=url, cookies=cookies)
print(response.text)

url = 'http://httpbin.org/post'
files = {'file': open('01-demo.py', 'rb')}

response = requests.post(url, files=files)
print(response.status_code)
print(response.content)

