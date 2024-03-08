my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

my_foods.insert(0,'pasta')
friend_foods.insert(2,'steak')

print('\nMy favorite foods are:')
for my_food in my_foods:
    print(my_food)

print('\nMy friend favorite foods are:')
for my_friend_food in friend_foods:
    print(my_friend_food)