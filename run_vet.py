from pet_class import *
from veterinarian_class import *
from appointment_class import *

# As a user I can create a pet
pet_list = []
pet1 = Pet('John Smith', 'Bubbles', 'Rabbit')
pet2 = Pet('Sarah Jane', 'Buttercup', 'Cat')
pet3 = Pet('Lindsay Lohan', 'King Cairo', 'Dog')
pet4 = Pet('Seth Rogan', 'Blossom', 'Hamster')

pet_list.append(pet1)
pet_list.append(pet2)
pet_list.append(pet3)
pet_list.append(pet4)

vet1 = Veterinarian('Torn ligaments', 'Dr. Wendy', 'Williams', '07336153421')
vet2 = Veterinarian('Flu jabs', 'Dr. Phil', 'Mitchell', '02085475475')
vet3 = Veterinarian('Indigestion', 'Dr. Caitlyn', 'Shameer', '01895466422')

appt1 = Appointment('Broken toe', '1 October 2019', '£85', vet1)
appt2 = Appointment('Blocked nose', '7 October 2019', '£45', vet2)
appt3 = Appointment('Lose bowel', '2 October 2019', '£30', vet3)

# As a user I can add a pet to appointment

booking1 = appt1.add_pet(pet1)
booking2 = appt2.add_pet(pet4)
booking3 = appt3.add_pet(pet3)

# As a user I can list all appointments (need to see what pet's are there)
# for booking in (appt1, appt2, appt3):
#     print(booking.appointment_info())

# As a user I can get pet details and owner details for a specific pet
# for pet in (pet1, pet2, pet3):
#     print(pet.pet_details())


user_name = input('Welcome to Pet Petrol!')
while True:
    print('What can I help you with?')
    print('(1) What appointments are on this week?')
    print('(2) What are your specialties here?')
    print('(3) Book a pet')
    user_input = input()
    if user_input == '1':
        print(appt1.appointment_info())
        print(appt2.appointment_info())
        print(appt3.appointment_info())
        break
    if user_input == '2':
        print(vet1.fullname(),'--', vet1.specialisation)
        print(vet2.fullname(),'--',vet2.specialisation)
        print(vet3.fullname(),'--', vet3.specialisation)
        break
    elif user_input == '3':
        owner_name = input('No problem, could I please have your full name?     ').strip()
        pet_disease = input('Cute name! could I ask what you are booking for?')
        pet_breed = input('What type of pet will you be bringing?')
        new_pet_info = Pet(pet_name,pet_disease,pet_breed)
        pet_list.append(new_pet_info)
        for pet in pet_list:
            print('Owner:', pet.owner, '--',  'Pet name:', pet.name, '--', 'Type of pet:', pet.breed)


