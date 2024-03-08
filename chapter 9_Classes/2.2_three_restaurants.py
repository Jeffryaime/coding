class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        """Initializing restaurant name and cuisine type"""
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        print(f"\nThe name of the restaurant is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

restaurant_one = Restaurant('thai express', 'thai cuisine')
restaurant_one.describe_restaurant()

restaurant_two = Restaurant('le serpent', 'italian cuisine')
restaurant_two.describe_restaurant()
 
restaurant_three = Restaurant('leméac', 'french cuisine')
restaurant_three.describe_restaurant()