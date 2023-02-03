current_users = ['john', 'sarah', 'mike', 'david', 'jane']
new_users = ['john', 'sophie', 'mike', 'katie', 'emily']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username {new_user} is already taken. Please enter a new username.")
    else:
        print(f"The username {new_user} is available.")
