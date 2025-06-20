# Page 166
class Restaurant:
    """
    Start with your program from Exercise 9-1 (page 162). 
    Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. 
    Print the number of customers the restaurant has served, and then change this value and print it again.
    """
    
    def __init__(self, name, cuisine_type, number_served=0):
        """Restaurant name and cuisine type"""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        
    def describe_number(self):
        """Print the number served"""
        people_served = f"Number Served: {self.number_served}"
        print(f"{people_served}")
    

customer1 = Restaurant('la pizzetta', 'italian', 35)

Restaurant.describe_number(customer1)
print(customer1.number_served)