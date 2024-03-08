def favorite_book(book_title):
    """Show my favorite book"""
    print(f"One of my favorite book is: {book_title.title()}")

favorite_book('rich dad & poor dad')

#Positional Arguments
def describe_animal(animal_type, pet_name):
    """Information about my animal"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_animal('dog', 'blacky')

#Order Matters in Positional Arguments

#Keyword Arguments

def describe_animal(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")
describe_animal(pet_name= 'willie', animal_type= 'tiger')

#Default Values

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f'I have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")
#describe_pet(pet_name='chase')
describe_pet('chase')

#Equivalent Functions Calls
