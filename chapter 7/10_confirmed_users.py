#Moving Items from One List to Another

unconfirmed_users = ['Alice', 'Brian', 'Candace']
confirmed_users = []

while unconfirmed_users:
    current_users = unconfirmed_users.pop()

    print(f"Verifying user: {current_users.title()}")
    confirmed_users.append(current_users)

print(f"\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(f"{confirmed_user.title()}")