class Users:
    """Storing information about the users"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def describe_user(self):
        print("\nHere is the summary of the user:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

class Admin(Users):
    """Providing admin information"""
    def __init__(self, first_name, last_name, privileges):
        """Initializing attibute of