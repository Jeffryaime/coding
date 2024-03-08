#voting.py
#age = 19
#if age >= 18:
    #print('You are old enough to vote!')
   # print('Have you registered yet to vote?')

#if-else statements

#age = 17
#if age >= 18:
  #  print()
#else:
#    print("Sorry, you are too young to vote!")
#    print("Please register to vote as soon as you turn 18!")

#if-elif-else chain
age = 65

#if age < 4:
#    print('Your admission cost is: 0.')
#elif age < 18:
#    print('Your admission cost is: $25')
#else:
#    print('Your admission cost is: $40.')

#if age < 4:
#    price = 0
#elif age < 18:
#    price = 25
#else:
#    price =40
#print(f'Your admission cost is: ${price}')

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f'Your admission cost is: ${price}')
#elif can substitute else statement
#example  elif age >= 65:
#               price = 20 can replace the else method on previous excercise.

#testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
#if want one block of code to run, use an if-elif-else chain. If more than one
#one block of code needs to run, use a series of indepedent if statements.