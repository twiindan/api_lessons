class ModifyUser(object):

    def __init__(self, username=None, email=None, about_me=None):
        self.username = username
        self.email = email
        self.about_me = about_me

    def to_dict(self):
        return{'username': self.username,
               'email': self.email,
               'about_me': self.about_me
               }
