#Looping through a Dictionary
# Looping through all the keys in a Dictionary
user_0 = {
    'username': 'enfermi',
    'first': 'enrico',
    'last': 'fermi',
    }

#for key, value in user_0.items():
#    print(f'\nKey: {key}')
#    print(f'Value: {value}')


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
#for name, language in favorite_languages.items():
 #   print(f"{name.title()}'s favorite language is {language.title()}.")

#Looping Through All the Keys in a Dictionary

#for name in favorite_languages.keys():
   # print(name.title())

#friends = ['phil', 'sarah']
#for name in favorite_languages.keys():
#    print(f"Hi {name.title()}")

#    if name in friends:
 #       language = favorite_languages[name].title()
 #       print(f"\tHi {name.title()}, I see you love {language}!")

#if 'erin' not in favorite_languages.keys():   #looping with keys() method
#    print('Erin please take our poll!')

#Looping Through a Dictionary's Keys in a Particular Order

#for name in sorted(favorite_languages.keys()):
#    print (f"{name.title()}, thank you for taking the poll")

#Looping Through All Values in a Dictionary

#print("The following languages have been mentioned:")
#for language in favorite_languages.values():
#    print(language.title())

#wrap set() around a collection to remove any duplicaton of data

for language in set(favorite_languages.values()):
    print(language)
