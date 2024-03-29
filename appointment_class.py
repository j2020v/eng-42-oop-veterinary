# This class will contain the attributes: disease, date, pet, vet, price

class Appointment():
    def __init__(self, disease, date, price, vet):
        self.disease = disease
        self.date = date
        self.price = price
        self.vet = vet
        self.pet_list = []

    def add_pet(self, pet):
        self.pet_list.append(pet)

    def get_vet(self):
        return self.vet

    def appointment_info(self):
        all_pets = []
        for pet in self.pet_list:
            all_pets.append(pet.owner)
            return f'Name: {pet.name}. Breed: {pet.breed}. In for: {self.disease}. Appointment date: {self.date}. Fee: {self.price}. Vet: {self.get_vet().fname}'

    def vet_info(self):
        for veterinarian in self.vet:
            return f'Vet Name: {self.get_vet().fullname}'



