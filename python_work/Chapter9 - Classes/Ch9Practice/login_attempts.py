class User:
    """
    Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
    Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
    Write another method called reset_login_attempts() that resets the value of login_attempts to 0. 
    Make an instance of the User class and call increment_login_attempts() several times. 
    Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
    Print login_attempts again to make sure it was reset to 0.
    """
    
    def __init__(self, first_name, last_name, user_name, login_attempts):
        """First name and last name attributes"""
        self.first = first_name.title()
        self.last = last_name.title()
        self.user = user_name

    
    def describe_user(self):
        """Print the description"""
        user_info = f"First name is {self.first}. Last name is {self.last}. Username is {self.user}."
        print(f"\n{user_info}")
    
    def greet_user(self):
        """Greet the user"""
        full_name = f"{self.first} {self.last}"
        print(f"Hello, {full_name}!")
    
    def increment_login_attempts(self):
        """Increments login attempts by 1"""