def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        print(f"Hi {name.title()}")

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)