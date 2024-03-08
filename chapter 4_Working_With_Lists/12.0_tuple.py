#tuple is a list that is immutable
dimensions = (200,50)
print(dimensions)
print(dimensions[0])
print(dimensions[1])
 #define a tuple with one element
my_t = (3,)  #tuple is defined by the presence of a comma
print(my_t)

for dimension in dimensions:
    print(dimension)

#writing over a Tuple
dimensions = (200,50)
print('Original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)    #assign new value
print('\nModified dimensions:')
for dimension in dimensions:
    print(dimension)


