class ForumMessage(object):

    def __init__(self, theme=None, subject=None, message=None):
        self.theme = theme
        self.subject = subject
        self.message = message

    def to_dict(self):
        return vars(self)
