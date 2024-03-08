alien_color = 'red'

if alien_color == 'green':
    print('You earned 5 points.')
elif alien_color == 'yellow':
    print('You earned 10 points.')
else:
    print('You have not earned any points.')

if alien_color != 'green':
    print('You earned 5 points.')
elif alien_color == 'yellow':
    print('You earned 10 points.')
else:
    print('You have not earned any points.')

if alien_color == 'green':
    print('You earned 5 points.')
elif alien_color != 'yellow':
    print('You earned 10 points.')
else:
    print('You have not earned any points.')