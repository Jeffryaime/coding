current_users = ['denzel', 'jennifer', 'bill', 'nia', 'gina']
current_users_lower = [user.lower() for user in current_users]

new_users = ['shaq', 'jennifer', 'selena','gina', 'drake', 'Denzel']
new_users_lower = [new_user.lower() for new_user in new_users ]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print('You need to enter a new username')
    else:
        print('The username is available')