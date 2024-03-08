#Using int() to Accept Numerical Input

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"Hello, {name}!")

age = input("How old are you? ")
age = int(age)

if age >= 18:
      print("\nYou are old enough to vote")
else:
    print("\nSorry, you cannot vote yet")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

