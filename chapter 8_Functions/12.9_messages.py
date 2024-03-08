def show_message(instructions):
    """Showing messages to users"""
    print(f"\nPlease pay atention to the listed instructions:")

    for message in instructions:
        print(f'{message.title()}')
        
messages = ['do not enter', 'turn right', 'continue straight', 'stop right there']
show_message(messages)