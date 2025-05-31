# page 150
# Storing your functions in a separate file called a module and then importing that module into your main program.
# Import statement tells python to makle the code in a module available in the currently running program file.


# Take function from pizza.py
# Add to making_pizza.py
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make.""" 
    print(f"\nMaking a {size}-inch pizza with the following toppings:") 
    for topping in toppings: 
        print(f"- {topping}")


        