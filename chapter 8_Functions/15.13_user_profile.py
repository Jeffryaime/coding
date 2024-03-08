def user_profile(first, last, **my_profile):
    """Collecting my personal profile in a dictionary"""
    my_profile['first name'] = first 
    my_profile['last name'] = last
    return my_profile

my_record = user_profile('jeff', 'prince',
                         edad = 33,
                         height = 5.11,
                         degree = 'business administration')

print(my_record)