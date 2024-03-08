class Users:
    def __init__(self, first_name, last_name):
        self.first_name = first_name.title()
        self.last_name = last_name.title()

    def describe_user(self):
        print("\nHere is the summary of the user:")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")

user = Users('jeff', 'prince')
 
user_two = Users('jean marc', 'kenley pierre')

user_three = Users('jennifer', 'lopez')

user.describe_user()
user.greet_user()

user_two.describe_user()
user_two.greet_user()

user_three.describe_user()
user_three.greet_user()