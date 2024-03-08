class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        """Initializing restaurant name and cuisine type, adding number served"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Providing restaurant name and cuisine type"""
        print(f"The name of the restaurant is {self.restaurant_name.title()}.")
        print(f"The cuisine type is {self.