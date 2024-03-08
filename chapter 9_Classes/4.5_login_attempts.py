class Users:
    def __init__(self, first_name, last_name):
        """Initializing user information"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.login_attempts = 0

    def describe_user(self):
        """Displaying users first and last name"""
        print("\nHere is the summary of the user:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Login Attempt: {self.login_a