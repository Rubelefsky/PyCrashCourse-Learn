# Page 162
class User:
    """Create 2 attributes"""
    
    def __init__(self, first_name, last_name):
        """First name and last name attributes"""
        self.first = first_name.title()
        self.last = last_name.title()
    
    def describe_user(self):
        """Print the description"""
        user_info = f"First name is {self.first}"
        print(f"\n{user_info}")

user_1 = User('brandon', 'rubell')
user_1.describe_user()


