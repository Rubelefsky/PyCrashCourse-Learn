# Page 162 - 

class Restaurant:
    """A class representing a restaurant"""
    
    def __init__(self, name, cuisine_type):
        """Restaurant name and cuisine type"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        message = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{message}")

    def open_restaurant(self):
        """Display a message that the restaurant is open!"""
        message = f"{self.name} is open!"
        print(f"{message}")

la_pizzetta = Restaurant('la pizzetta', 'italian')
la_pizzetta.describe_restaurant()

marios = Restaurant('marios pizza', 'pizza')
marios.describe_restaurant()

sophies = Restaurant('sophies cuban', 'cuban')
sophies.describe_restaurant()