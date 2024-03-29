#Modify incremented method to reject negative increments to prevent roll back.
class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attemps to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        if miles < 0:
            print("You can't roll back on odometer!")
        else:
            self.odometer_reading += miles

my_used_car = Car('edge', 'ford', 2023)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(150)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

 