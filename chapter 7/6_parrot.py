#Letting the User Choose When to Quit

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
        #1) print(message)

    if message != 'quit':
        print(message)