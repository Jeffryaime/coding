my_pizzas =['pepperoni', 'hawaiian', 'meat lovers']
friend_pizzas = my_pizzas[:]
my_pizzas.append('bbq chicken')
friend_pizzas.append('veggie')
print('My favorite pizzas are:')
for my_pizza in my_pizzas:
    print(my_pizza)
print("My friend's favorite pizzas are:")
for my_friend_pizza in friend_pizzas:
    print(my_friend_pizza)