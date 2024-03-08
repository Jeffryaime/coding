#Nesting
#alien_0 = {'color': 'green', 'points':5}
#alien_1 = {'color': 'yellow', 'points':10}
#alien_2 = {'color': 'red', 'points': 15}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
   # print(alien)

#make 30 green aliens
aliens = []

for alien_number in range(30):
    new_alien = {'color':'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
#print(f"The total number of aliens: {len(aliens)}")

for alien in aliens[:3]:
    if alien['color']== 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium-high'
    
#for alien in aliens[:5]:
#    print(alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium-high'
        alien['points'] = '10'        
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'
        
for alien in aliens[:3]:
    print(alien)

#A list in a Dictionary
pizza = {
     'crust': 'thick',
     'toppings': ['mushrooms', 'extra cheese']
    }
print(f"\nYou ordered a {pizza['crust']}-crust pizza"
      " with the following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

#favorite_languages.py
favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }
for name,languages in favorite_languages.items():
    if len(languages) < 2:
        print(f"{name.title()}'s favorite language is:")
    if len(languages) >= 2: 
        print(f"{name.title()}'s favorite language are:")
    for language in languages:
        print(f"\t{language.title()}")

#A Dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")