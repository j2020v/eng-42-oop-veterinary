# This is a class and should have owner, name and breed as its attributes

class Pet():
    def __init__(self, owner, name, breed):
        self.owner = owner
        self.name = name
        self.breed = breed


# As a user I can get pet details and owner details for a specific pet
    def pet_details(self):
        return f'Name of pet: {self.name}. Owner: {self.owner}. Breed: {self.breed}'