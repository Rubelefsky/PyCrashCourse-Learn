class Dog: # Define a class named dog. Capitalized names refer to classes in Python.
    """A  simple attempt to model a dog"""
    # A function that is part of a class is called a method.

    def __init__(self, name, age): # _init_ is a special method that Python runs automatically whenever we a create a new instance based on the dog class.
        # The underscores before and after is a convention that helps prevent Pythons default method names from conflicting with your method names.
        """initialize name and age attributes"""
        self.name = name
        self.age = age
        # Variables that are accessible through instances are called attributes.

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
        