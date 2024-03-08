class Users:
    """Storing information about the users"""
    def __init__(self, first_name, last_name):
        """Initializing the storing of users info."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def describe_user(self):
        """Describing user info"""
        print("\nHere is the summary of the user:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

    def greet_user(self):
        """Greeting the user"""
        print(f"Hello {self.first_name} {self.last_name}")

class Admin(Users):
    """Providing admin information"""
    def __init__(self, first_name, last_name, privileges):
        """Initializing attibute of the parent class.
        Then initializing attribute that store of a list of strings.
        """
        super().__init__(first_name, last_name)
        self.privileges_attribute = Privileges(privileges)

class Privileges:
    """A simple class to manage the privileges"""
    def __in