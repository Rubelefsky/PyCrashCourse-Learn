# Page 162
class Car: # Create car class
    """A class representing a car."""
    def __init__(self, make, model, year): # assigns parameters to attributes that will associated with instances
        self.make = make
        self.model = model
        self.year = year
    
    def get_descriptive_name(self): # puts all info in 1 string
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    

my_new_car = Car('audi', 'r8', '2025') # my_new_car instance
print(my_new_car.get_descriptive_name()) # call get_descriptive name with instance my_new_car