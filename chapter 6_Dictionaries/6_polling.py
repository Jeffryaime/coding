favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

people = ['sarah', 'denzel', 'edward', 'jayden']

for name in favorite_languages.keys():
    if name in people:
        print(f'Hi {name.title()}, thank you for responding')
    else:
        print(f'Hi {name.title()}, please take the poll asap.')