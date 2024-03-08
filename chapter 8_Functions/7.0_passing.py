#Passing a List

def greet_user(names):
    """print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
    
usernames = ['katia', 'carter', 'coise']
greet_user(usernames)

#Modifying a List in a Function
