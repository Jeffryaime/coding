#the list
languages = ['creole','english','french','german','portuguese','russian','bengali','hindi']
#print the list
print(languages)
#accessing elements in the list
print(languages[0].title())
print(languages[1].title())
print(languages[2].title())
#using individual value from the list
message = f'{languages[0].title()} is my mother tongue language.'
print(message)
#modifying a value in the list
languages[0] = "spanish"
print(languages)
#adding values in the list

languages.append('mandarin') #appending elements to the end of a list
print(languages)

languages.insert(0,'italiano') #inserting elements into the list
print(languages)
#removing elements from the list
del languages[-1]  #del Statement
print(languages)

popped_language = languages.pop()  #pop() method - work with item removed
print(languages)
print(popped_language)
message = f'The second language from where I come from is: {popped_language.title()}'
print(message)
unspoken_language = languages.pop(0) #popping items from any Position in the list
message = f'I do not speak {unspoken_language.title()}'
print(message)

languages.remove('spanish')  #remove() 
print(languages)
love_language = 'french'     #remove() - with re-usable variable
languages.remove(love_language)
print(languages)
print(love_language)

print('\nThis is the second portion of this Chapter')
#Organizing the list
cities = ['port-au-prince','québéc','jacmel','arcahaie','bainet','london']
print(cities)
#cities.sort() #sorting the list alphabetically permanently with the sort() method
#print(cities)
#cities.sort(reverse=True) #reverse alphabetical sorting the list permanently with the reverse argument
#print(cities)
#sorting the list temporarily with the sorted() function
print(sorted(cities))

#sorting the list temporarily in reverse alphabetical order
first_visited = sorted(cities,reverse=True)
print(first_visited) 
print(cities)

#Printing a List in Reverse Order
cities.reverse()
print(cities)

#finding the Length of a List
message = len(cities)
message1 = len(languages)

print(f'I want to visit those : {message} cities.')
print(f'I want to speak those: {message1} languages.')