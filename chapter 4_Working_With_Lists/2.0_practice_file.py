#using numerical list
#range()
#for value in range(1,5):
   #  print(value)
#for value in range(1,6):
    #print(value)

#using range() to make a List of Numbers with list() function
#numbers = list(range(1,6))
#print(numbers)

#skip numbers in a given range
#even_numbers = list(range(2,11,2))
#print(even_numbers)

#square_number.py
squares = []
for value in range(1,11):
    #square = value ** 2
    squares.append(value ** 2)
print(squares)

# Python functions to find: minimum, maximum, sum of numbers
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehensions
squares = [value ** 2 for value in range(1,11)]
print(squares)