message = "What is your age "

active = True
while active:
    age = input(message)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("The ticket is free\n")
    elif age < 13:
        print("The ticket is $10\n")
    else:
        print("The ticket is $15\n")
    
        