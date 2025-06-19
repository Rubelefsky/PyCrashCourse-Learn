# Page 162
class Car: # Create car class
    """A class representing a car."""
    def __init__(self, make, model, year): # assigns parameters to attributes that will associated with instances
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # default value = 0
    
    def get_descriptive_name(self): # puts all info in 1 string
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self): # Print a statement showing the cars miles
        """Odometer reading"""
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage): # method that updates certain attributes
        """Set the odometer reading to the given value
            Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage # assigns self.odometer_reader a new value
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """
        Add the given amount to the odometer reading
        """
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2019)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()