# Page 146 - Continuation of pizza.py
def make_pizza(*toppings): # Create function called make_pizza. The * in the parameter name tells Python to make a tuple called toppings.
    """Summarize the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings: # loop through toppings
        print(f"- {topping}") # Print each topping

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')