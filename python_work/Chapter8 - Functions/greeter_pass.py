def greet_user(username): # Allow the function to accept any value of username you specify
    """Display a simple greeting.""" # docstring
    print(f"Hello, {username.title()}!")
# function now expects you to provide a value for username each time you call it
greet_user('jesse')
greet_user('brandon')