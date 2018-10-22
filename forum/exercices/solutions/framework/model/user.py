class User(object):

    def __init__(self, name=None, username=None, password=None, role=None, email=None):
        self.name = name
        self.username = username
        self.password = password
        self.role = role
        self.email = email

    def to_dict(self):
        return  {'name': self.name,
                'username': self.username,
                'password': self.password,
                'role': self.role,
                'email': self.email
                }
