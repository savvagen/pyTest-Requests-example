
def as_greeting(dct):
    return Greeting(dct['id'], dct['content'])


class Greeting(object):

    def __init__(self, id, content):
        self.id = id
        self.content = content