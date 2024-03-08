#Passing an Arbitrary Number of Arguments

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza("pepperoni")
make_pizza("mushrooms", "green peppers", "extra cheese")

#Mixing Positional an Arbitrary Arguments

def make_pizza(size, *toppings):  #the arbituary argument always last.
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, "pepperoni")
make_pizza(25,"mushrooms", "green peppers", "extra cheese")
