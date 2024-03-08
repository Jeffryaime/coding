#greet.py
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
greet_user()

#passing information to a Function
def greet_user(username):
    """ Display a simple greeting."""
    print(f"Hello, {username.title()}")
greet_user('jeff')
