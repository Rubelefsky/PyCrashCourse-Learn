# Page 162
class User:
    """Create 2 attributes"""
    
    def __init__(self, first_name, last_name, user_name):
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

brandon = User('brandon', 'rubell', 'brubell')
brandon.describe_user()
brandon.greet_user()




