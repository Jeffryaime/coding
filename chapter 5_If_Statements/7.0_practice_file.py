#using if Statements with Lists
#topping.py

#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

#for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print('Sorry we are out of green peppers')
#else:
 #       print(f'Adding {requested_topping}')
#print('\nFinished making your pizza')

#checking that a list is not empty

#requested_toppings = []

#if requested_toppings:          #checking with if and the list:
#    for requested_topping in requested_toppings:
#        print(f'Adding {requested_topping}')
#else:
#    print('Are you sure you want a plain pizza?')

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 
                      'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping} in your pizza')
    else:
        print(f'Sorry we do not have {requested_topping}')
print('\nFinished making your pizza')


