people_favorite_numbers = {
    'ylonne': [5148215472, 6148527845],
    'bibi': [3472997146, 9637895623, 7414589656],
    'valérie': [50936921027, 5487451245],
    'roro': [50937327758], 
    'guerline': [50946443404, 6689548525, 7894562312],
    }

for people, favorite_numbers in people_favorite_numbers.items():
    if len(favorite_numbers) >= 2:
        print(f"\n{people.title()}'s favorite numbers are:")
    else:
        print(f"\n{people.title()}'s favorite number is:")
    for favorite_number in favorite_numbers:
        print(f'{favorite_number}')

