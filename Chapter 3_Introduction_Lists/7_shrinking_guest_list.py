guest_lists = ['manman','grandma','papa']
guest_lists[2] = 'tante marie'

#print (guest_lists[2].title())
#print(guest_lists)

guest_lists.insert(0,'falonne')
#print(guest_lists)
guest_lists.insert(2,'jayden')
#print(guest_lists)
guest_lists.append('alyssa')
print(guest_lists)
invite2 = 'Mwen jwen yon pi gro table donk nap ka pi alez poun ka pase on pi bon moment ak tout fanmiy an'

message1 = f'Salut {guest_lists[0].title()}, {invite2}'
message2 = f'Salut {guest_lists[1].title()}, {invite2}'
message3 = f'Salut {guest_lists[2].title()}, {invite2}'
message4 = f'Salut {guest_lists[3].title()}, {invite2}'
message5 = f'Salut {guest_lists[4].title()}, {invite2}'
#print(message1)
#print(message2)
#print(message3)
#print(message4)
#print(message5)
print('I can only invite 2 people for dinner')

popped_guest1 = guest_lists.pop()
print(f'Mwen désolé {popped_guest1.title()}, mwen pap ka invitew anko nan dine a.')
popped_guest2 = guest_lists.pop()
print(f'Mwen désolé {popped_guest2.title()}, mwen pap ka invitew nan dine a anko.')
popped_guest3 = guest_lists.pop(0)
print(f'Mwen désolé {popped_guest3.title()}, mwen pap ka invitew nan dine a anko.')
popped_guest4 = guest_lists.pop(1)
print(f'Mwen désolé {popped_guest4.title()}, mwen pap ka invitew nan dine a anko.')

print(f'Bonjou {guest_lists[0].title()}, fok ou toujou vini nan dine a.')
print(f'Bonjou {guest_lists[1].title()}, fok ou toujou vini nan dine a.')

del guest_lists[0]
del guest_lists[0]

print(guest_lists)