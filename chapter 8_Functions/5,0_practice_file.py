#Return Values

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f'{first_name} {last_name}'
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#making an argument optional

def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('alyssa','iris','prince')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jayden', 'prince', 'asher')
print(musician)

#Returning a dictionary

def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jackie', 'chan')
print(musician)

#storing person's age and height

def build_person(first_name, last_name, age=None, height=None):
    """Return a dictionary with information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    if height:
        person['height'] = height
    return person
musician = build_person('whitney', 'houston', 50, 5.4)
print(musician)