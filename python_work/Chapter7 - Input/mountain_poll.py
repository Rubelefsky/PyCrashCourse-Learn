responses = {}

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store response in dictionary
    responses[name] = response
    
