class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        """Initializing restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name.title()}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open.")

restaurant = Restaurant('la banquise', 'Canadian Cuisine' )
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

        