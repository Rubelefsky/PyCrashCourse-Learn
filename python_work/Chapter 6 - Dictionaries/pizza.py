# Page 108
# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Summarize the order
print(f"You ordered a {pizza['crust']} - crust pizza "
      "with the following toppings:")
# When breaking up a long line in print
# choose an appropriate point at which to break the line being printed, and end the line with a quotation mark
# Indent the next line, add an opening quotation mark, and continue the string. 

for topping in pizza['toppings']: # For loop, use key - toppings
    print(f"\t{topping}")