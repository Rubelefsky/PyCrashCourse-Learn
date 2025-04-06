# page 124

# start with users that need to be verififed
# and en ampty list to hold confirmed users

unconfirmed_users = ['brandon', 'jacob', 'steve']
confirmed_users = []

# verify each user until there are no more unconfirmed users
# move each verified user into the list of confirmed users

while unconfirmed_users:
    current_user = unconfirmed_users.pop() # remove from unconfirmed users and add to current_users variable

    print(f"Verifying user: {current_user.title()}") # print the popped users
    confirmed_users.append(current_user) # add the user to the confirmed users list

    # DIsplay all confirmed users

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users: # For each user in the new list
    print(confirmed_user.title()) # Print the user with title (caps)
