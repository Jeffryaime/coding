def city_country(city_name, country):
    """Return a formatted string"""
    string = f'"{city_name}", "{country}"'
    return string.title()

location = city_country('miami', 'united states of america')
print(location)