def show_message(instructions):
    """Showing messages to users"""
    print(f"\nPlease pay atention to the listed instructions:")

    for message in instructions:
        print(f'{message.title()}')