# PAge 149 
# 8.12 
def build_sandwich(bread, **ingredients):
    """ 
    Write a function that accepts a list of items a person wants on a sandwich. 
    The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sand- wich that’s being ordered. 
    Call the function three times, using a different num- ber of arguments each time.
    """
    ingredients['bread_type'] = bread
    return ingredients

sandwich_type1 = build_sandwich('ciabatta', condiments='ketchup', meat='turkey', cheese='swiss')
print(sandwich_type1) 

sandwich_type2 = build_sandwich('whole wheat', veggies='tomato')
print(sandwich_type2)

hamburger = build_sandwich('potato roll', meat='ground beef', condiments='ketchup', cheese='american')
print(hamburger)