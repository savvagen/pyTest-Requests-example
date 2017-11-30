
class User(object):

    def __init__(self, email, fullname, password, username):
        self.email = email
        self.fullname = fullname
        self.password = password
        self.username = username

    def setEmail(self, email):
        self.email = email

    def setPassword(self, password):
        self.password = password

    def setFullname(self, fullname):
        self.fullname = fullname

    def setUsername(self, username):
        self.username = username

    # @property
    # def fullname(self):
    #     return self.fullname
    #
    # @property
    # def email(self):
    #     return self.email
    #
    # @property
    # def password(self):
    #     return self.password
    #
    # @property
    # def username(self):
    #     return self.username
