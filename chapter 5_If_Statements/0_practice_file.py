#cars.py
#*cars = ['audi', 'bmw', 'subaru', 'toyota']
#*for car in cars:
    #*if car == 'bmw':
        #*print(car.upper())
    #*else:
        #*print(car.title())

#conditional tests: evaluation a True or False
#case sensitive / can convert to make insensitive

#toppings.py
#*requested_topping = 'mushrooms'
#*if requested_topping != 'anchovies':
    #*print('Hold the anchovies!')

#numerical comparisons
#magic_number.py
#*answer = 17
#*if answer != 42:
    #*print('This is not the correct answer. Please try again!')

#*age = 19
#*if age >= 21:
    #*print('Yes')
#*else:
    #*print('No, that is the wrong answer!')

#checking multiple conditions at the same time with keyword 'and'
#*eage_0 = 22
#*eage_1 = 18
#*eif (age_0 >= 21) and (age_1 >= 21):
    #*eprint('True')
#*eelse:
   #*e print('False')

#checking multiple condition either or with keyword 'or'
#*eage_0 = 18
#*eage_1 = 18
#*eif (age_0 >= 21) or (age_1 >= 21):
   #*e print('True')
#*eelse:
   #*e print('False')

#checking whether a value is is a list with keyword 'in'
#*requested_toppings = ['mushrooms', 'onions', 'pineapple']
#*if 'Mushrooms'.lower() in requested_toppings:
#*print('True')
#*else:
 #*   print('False')

#checking whether a value is not is a list with keyword 'not in'

banned_users = ['Andrew', 'carolina', 'david']
user = 'Falonne'
 
print(banned_users)

if user.lower() not in [user.lower() for user in banned_users]:
    print(f'{user.title()}, you can post a response if you wish')

#*banned_users_lower = []
#*for user in banned_users:
  #*  converted = user.lower()
 #*   banned_users_lower.append(converted)
#*if user not in banned_users_lower:
    #*print(f'{user.title()}, you can post a response if you wish)