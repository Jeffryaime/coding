def describe_city(city_name, country='canada'):
    """Information about cities"""
    print(f"{city_name.title()} is in {country.title()}.")
describe_city('montreal')
describe_city('toronto')
describe_city(country= 'france', city_name= "paris")