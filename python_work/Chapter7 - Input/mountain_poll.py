responses = {}

# set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store response in dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no)") # set variable repeat - yes or no input
    if repeat == 'no': # if repeat is == to no
        polling_active = False # make the flag false (not active)
        
    # polling is complete. Show the results.
    print("\n--- Poll Results ---")
    for name, response in responses.items(): # for the name and response (mountain) # sets a key-value pair
        print(f"{name.title()} would like to climb the {response.title()}.")