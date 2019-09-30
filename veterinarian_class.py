# This class will be a sub-class of the human and will inherit its attributes
# We will add specialisation as an added attribute
from human_class import *

class Veterinarian(Human):
    def __init__(self, specialisation, fname, lname, phone):
        super().__init__(fname, lname, phone)
        self.specialisation = specialisation 