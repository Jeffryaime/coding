dream_vacation = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    dream_vacation[name] = response

    repeat = input('Would you like to let another person answer? (yes/no)')

    if repeat == 'no':
        polling_active = False

print("\n----Polling Results----")

for name, response in dream_vacation.items():
    print(f"If {name.title()} could visit one place in the world "
          f"that would be {response.title()}")