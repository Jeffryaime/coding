prompt = "\nEnter a series of pizza toppings "
prompt += "\n(Enter quit when finish) "

message = input(prompt)
while message == "quit":
    break
else:
    print(f"I will add the {message} to your pizza")