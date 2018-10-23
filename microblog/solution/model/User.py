class User(object):

    def __init__(self, username=None, password=None, email=None):
        self.username = username
        self.password = password
        self.email = email

    def to_dict(self):
        return{'username': self.username,
               'password': self.password,
               'email': self.email
               }
