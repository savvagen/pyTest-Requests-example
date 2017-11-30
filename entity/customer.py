

def as_customer(dct):
    return Customer(dct['email'], dct['id'], dct['firstName'], dct['lastName'])

class Customer(object):

    def __init__(self, email, id, firstName, lastName):
        self.email = email
        self.id = id
        self.firstName = firstName
        self.lastName = lastName