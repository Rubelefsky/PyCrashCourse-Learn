favorite_toppings = ['pepperoni', 'chicken', 'sausage'] # Create list
topping = 'chicken' # assign cicken to topping variable
if topping in favorite_toppings: # if topping is in list print below
    print(f"{topping.title()} is my favorite topping!")
topping = 'mushroom' # change variable to mushroom
if topping not in favorite_toppings: # if not in the list of favorite toppings print below
    print(f"\n{topping.title()} is not my favorite topping!")
