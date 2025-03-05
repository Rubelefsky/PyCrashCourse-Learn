banned_users = ['brandon', 'scott', 'steven'] # Create a list called banned_users
user = 'brandon' # user variable assigned to brandon
if user not in banned_users: # If user not in list
    print(f"{user.title()}, you can post a response if you wish.") # Print if True
else:
    print(f"{user.title()}, you cannot post a response.") # Print if false

