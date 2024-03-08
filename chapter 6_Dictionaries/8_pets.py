neighors_pet = {
    'kind_animal': 'dog',
    "owner_name": 'paul',
    }
mommy_pet = {
    'kind_animal': 'cat',
    'owner_name': 'ilonne'
    }
book_pet = {
    'kind_animal': 'frog',
    'owner_name': 'neville',
    }
pets = [neighors_pet, mommy_pet, book_pet]

print(f"\nHere is the pets information list:\n")
for animals in pets:
    print(f"Kind of Animal: {animals['kind_animal']}")
    print(f"Owner's Name: {animals['owner_name'].title()}\n")