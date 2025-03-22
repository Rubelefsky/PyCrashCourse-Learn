# 6.8 Make several dictionaries, representing a different pet.
pets = {
    'dog': {
        'breed': 'poodle',
        'name': 'corduroy'
    },
    'cat': {
        'breed': 'calico',
        'name': 'jackson'
    }
}

pet_list = [pets['cat'], pets['dog']]

for pet, pet_info in pets.items():
   # print(f'\nPet: {pet.title()}')
   # print(f'Breed: {pet_info['breed'].title()}')
   # print(f'Name: {pet_info['name'].title()}')

   print(f'\nPet: {pet.title()}\nBreed: {pet_info['breed'].title()}\nName: {pet_info['name'].title()}')

# This is def not right - I need to re do this dictionaries chapter.