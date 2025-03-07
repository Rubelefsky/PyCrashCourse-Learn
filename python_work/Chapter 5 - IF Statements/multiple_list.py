available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese'] # List called available toppings

requested_toppings = ['mushrooms', 'french fries', 'extra cheese'] # list called requested_toppings

for requested_topping in requested_toppings: # First loop through requested toppings
    if requested_topping in available_toppings: # Check to see if in available toppings list
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, We don't have {requested_topping}.") # if topping is not in available_toppings list print message

print("\nFinished making your pizza!")