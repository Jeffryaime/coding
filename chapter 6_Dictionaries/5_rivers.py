rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
    }

for river,country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print('\nHere is the list of the name of each river:')
for river in rivers.keys():
    print(f'{river.title()}')

print('\nHere is the list of the name of each country:')
for country in rivers.values():
    print(f"{country.title()}")