son_info = {
    'first_name': 'jayden',
    'last_name': 'prince',
    'age': 4,
    'city': 'montreal'
    }

wife_info = {
    'first_name': 'falonne',
    'last_name': 'st georges',
    'age':31,
    'city': 'montreal'
    }

husband_info = {
    'first_name': 'jeff',
    'last_name': 'prince',
    'age': 33,
    'city': 'montreal'
    }

people = [son_info, wife_info, husband_info]

print("\nHere is the Prince's family:\n")
for family in people:
    print(f"First Name: {family['first_name'].title()}")
    print(f"Last Name: {family['last_name'].title()}")
    print(f"Age: {family['age']}")
    print(f"City: {family['city'].title()}\n")

 
