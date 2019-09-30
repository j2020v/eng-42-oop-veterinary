# This is a sub-class of the human class and will inherit its attributes
# We will add payment_details as an added attribute
from human_class import *
class Client(Human):
    def __init__(self, payment_details, fname, lname, phone):
        super().__init__(fname, lname, phone)
        self.payment_details = payment_details