available_usernames = ['admin', 'brandon', 'jack', 'smith', 'steve'] # Create a list

for username in available_usernames: # loop through list of usernames
    if username == 'admin': # if username is equal to admin, print below
        print(f"Welcome, {username.title()}, Would you like a status report?")
    elif username in available_usernames:# if username is in list and not admin, print below
        print(f"Welcome, {username.title()}. Thank you for logging in.")
    else: # if username is not in list, print below
        print(f"{username} is an incorrect username.")