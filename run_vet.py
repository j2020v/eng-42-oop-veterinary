from pet_class import *
from veterinarian_class import *
from appointment_class import *

# As a user I can create a pet
pet1 = Pet('John Smith', 'Bubbles', 'Rabbit')
pet2 = Pet('Sarah Jane', 'Buttercup', 'Cat')
pet3 = Pet('Lindsay Lohan', 'King Cairo', 'Dog')
pet4 = Pet('Seth Rogan', 'Blossom', 'Hamster')

vet1 = Veterinarian('Torn ligaments', 'Dr. Wendy', 'Williams', '07336153421')
vet2 = Veterinarian('Flu jabs', 'Dr. Philip', 'Mitchel', '02085475475')
vet3 = Veterinarian('General', 'Dr. Caitlyn', 'Shameer', '01895466422')

appt1 = Appointment('Broken toe', '1 October 2019', '£85', vet1)
appt2 = Appointment('Blocked nose', '7 October 2019', '£45', vet2)
appt3 = Appointment('General check-up', '2 October 2019', '£30', vet3)

# As a user I can add a pet to appointment
booking1 = appt1.add_pet(pet1)
booking2 = appt2.add_pet(pet4)
booking3 = appt3.add_pet(pet3), appt3.add_pet(pet2)


# As a user I can list all appointments (need to see what pet's are there)
for pet in (booking1, booking2, booking3):
    print(appt3.appointment_info())


# As a user I can list all appointments (need to see what pet's are there)

# As a user I can add a pet to appointment
    # Create a method that allows us to add a pet using .append()



# As a user I can get pet details and owner details for a specific pet
    # Create a method that lists owner details and pet details