available_usernames = ['admin', 'brandon', 'jack', 'smith', 'steve'] # Create a list

if available_usernames:
    for username in available_usernames: # loop through list of usernames
        if username == 'admin': # if username is equal to admin, print below
            print(f"Welcome, {username.title()}, Would you like a status report?")
        elif username in available_usernames:# if username is in list and not admin, print below
            print(f"Welcome, {username.title()}. Thank you for logging in.")
else: # if username is not in list, print below
    print(f"We need to find some users.")

# 5.9 No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# Tested by removing users from list and else statement did print


