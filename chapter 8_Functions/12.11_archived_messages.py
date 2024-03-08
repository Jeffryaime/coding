def show_message(instructions):
    """Showing messages to users"""
    print(f"\nPlease pay atention to the listed warnings:")

    for message in instructions:
        print(f'{message.title()}')
    print()

def send_messages(messages, sent_messages):
    """Printing & Sending messages to user"""
    while messages:
        printing_messages = messages.pop()
        print('Printing the following instruction:')
        print(f"{printing_messages.title()}")
        sent_messages.append(printing_messages)

    print('\nFollowing message has been sent:')
    for sent_message in sent_messages:
        print(f"{sent_message.title()}")

messages = ['do not enter', 'turn right', 'continue straight', 'stop right there']
sent_messages = []

send_messages(messages [:], sent_messages)


print(f"\nOriginal List: {messages}")
print(f"List Copy: {messages[:]}")