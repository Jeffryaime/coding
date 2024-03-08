clothes = ['pants', 'shirts', 't-shirts', 'hats']
for cloth in clothes:
    if cloth == 'pants':
        print('I predict True')
    else:
        print( 'I predict False')

for cloth in clothes:
    if cloth != 'pants':
        print('I can see True')
    else:
        print('I can see False')

animals = ['cat', 'dog', 'tiger']

for animal in animals:
    if animal.lower() == 'cat':
        print('This is True')
    else:
        print('This is False')

animals = ['cat', 'dog', 'tiger']
animal = 'lion'

if animal not in animals:
    print('This animal is not in the list')

a = 12
b = 21

if a < b:
    print('That is correct')
else:
    print('That is not correct')

if a > b:
    print('That is correct')
else:
    print('That is not correct')

if a >= b:
    print('That is correct')
else:
    print('That is not correct')

c = 10

if c == 10:
    print('Yes')

if c <= 10:
    print('Yes')

if c < 10:
    print('Yes')
else:
    print('No')

if c != 10:
    print("It's not equal")
else:
    print("It's equal")
