# This is a class and should have owner, name and breed as its attributes

class Pet():
    def __init__(self, owner, name, breed):
        self.owner = owner
        self.name = name
        self.breed = breed

    def flight_details(self):
        all_pass = []
        for passenger in self.passenger_list:
            all_pass.append(passenger.fullname())
        return f'{self.flight_number} is going to {self.get_destination()} from {self.get_origin()}. Flight time: {self.time}.'\
    f' Calling all passengers: {all_pass} - Passport number: {self.get_passport()}'

# As a user I can get pet details and owner details for a specific pet
    def pet_details(self):
        return f'Name of pet: {self.name}. Owner: {self.owner}. Breed: {self.breed}.'