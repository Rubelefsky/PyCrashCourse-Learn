requested_toppings = [] # Empty List

if requested_toppings: # Returns true if List contains atleast one item. False if none
    for requested_topping in requested_toppings: # if the conditional test passes, we print the toppings
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print('Are you sure you want a plain pizza?') # Else print message