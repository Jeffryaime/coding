#alien_0 = {'color': 'green', 'points': '5'}

#print(alien_0['color'])
#print(alien_0['points'])

#new_points = alien_0['points']
#print(f'You just earned {new_points} points!')

#adding new key-value pairs
#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)

#starting with an Empty Dictionary
#alien_0 = {}

#alien_0['color'] = 'green'
#alien_0['points']= 5

#print(alien_0)

#Modifying Values in a Dictionary
#print(f'The alien is now {alien_0["color"]}')

#alien_0['color'] = 'yellow'
#print(f'The alien is now {alien_0["color"]}')

#print(alien_0)

#alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#print(f'Original position: {alien_0['x_position']}')

#alien_0['speed'] = 'fast'

#if alien_0['speed'] == 'low':
#    x_increment = 1
#elif alien_0['speed'] == 'medium':
#    x_increment = 2
#else:
#    x_increment = 3
#alien_0['x_position'] = alien_0['x_position'] + x_increment
#print(f'New position: {alien_0["x_position"]}')

#Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
#print(alien_0)

del alien_0['points']
#print(alien_0)

#A Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',    
    }
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is: {language}")

#Using get() to Access Values

alien_0 = { 'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points','No point value assigned.')
print(point_value)