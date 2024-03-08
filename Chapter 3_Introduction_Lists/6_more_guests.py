guest_lists = ['mom','grandma','papa']
invite = 'sa fè lontan nou pa wè, kijan ou ye? mta renmen invite ou vin manje lakay la. Map tann repons ou. I love you'
guest_lists[2] = 'tante marie'
#message1 = f'Bonjour {guest_lists[0].title()},{invite}'
#message2 = f'Bonjour {guest_lists[1].title()},{invite}'
#message3 = f'Bonjour {guest_lists[2].title()},{invite}'
print (guest_lists[2].title())
print(guest_lists)
#print(message1)
#print(message2)
#print(message3)
guest_lists.insert(0,'falonne')
print(guest_lists)

guest_lists.insert(2,'jayden')
print(guest_lists)
guest_lists.append('alyssa')
print(guest_lists)
invite2 = 'Mwen jwen yon pi gro table donk nap ka pi alez poun ka pase on pi bon moment ak tout fanmiy an'

message1 = f'Salut {guest_lists[0].title()}, {invite2}'
message2 = f'Salut {guest_lists[1].title()}, {invite2}'
message3 = f'Salut {guest_lists[2].title()}, {invite2}'
message4 = f'Salut {guest_lists[3].title()}, {invite2}'
message5 = f'Salut {guest_lists[4].title()}, {invite2}'

print(message1)
print(message2)
print(message3)
print(message4)
print(message5)