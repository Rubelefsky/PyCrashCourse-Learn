# 5.10 Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username
current_users = ['admin', 'brandon', 'jack', 'smith', 'steve']

copy_current_users = current_users[:]

new_users = ['brandon', 'bob', 'smith', 'jim', 'alex']

for users in new_users: # For users in New users list
    if users in current_users: # If user is also in current list
        print(f"Hello, that user name {users} is taken.")
    if users not in current_users:
        print(f"That username {users} is available.") # print - brandon and smith

# Loop through the new_users list to see if each new username has already been used. 
# If it has, print a message that the person will need to enter a new username. 
# If a username has not been used, print a message saying that the username is available.
# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. 
# (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)