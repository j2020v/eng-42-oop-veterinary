# This is a parent class and should have: name, phone and email

class Human():
    def __init__(self, fname, lname, phone):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = fname + '.' + lname +'@company.com'
