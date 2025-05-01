# Page 142 - Passing a list to a function
def greet_users(names):
    """Print a sample greeting to each user in the list."""
    for name in names: # Cycle through the list
        msg = f"Hello, {name.title()}!" # variable is set to say Hello and each name
        print(msg) # print the variable

usernames = ['hannah', 'ty', 'margot'] # create the list
greet_users(usernames) # passes the list through the function

new_users = ['brandon', 'scott', 'steve']
greet_users(new_users)

new_users_test = ['test1', 'test2', 'test3']
greet_users(new_users_test)