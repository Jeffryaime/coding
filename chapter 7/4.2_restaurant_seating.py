people = input("How many people are in your dinner group? ")
people = int(people)

if people > 8:
    print(f"You will need to wait for a table.")
else:
    print(f"Your table is ready.")