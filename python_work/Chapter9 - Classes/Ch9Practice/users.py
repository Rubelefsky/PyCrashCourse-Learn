# Page 162
class User:
    """Create 2 attributes"""
    
    def __init__(self, first_name, last_name, user_name, email, location):
        """First name and last name attributes"""
        self.first = first_name.title()
        self.last = last_name.title()
        self.user = user_name
        self.email = email
        self.location = location

    
    def describe_user(self):
        """Print the description"""
        print(f"\n{self.first} {self.last}")
        print(f"    Username: {self.user}")
        print(f"    Email: {self.email}")
        print(f"    Location: {self.location}")

    
    def greet_user(self):
        """Greet the user"""
        full_name = f"{self.first} {self.last}"
        print(f"\nHello, {full_name}!")

brandon = User('brandon', 'rubell', 'brubell', 'brubell@gmail.com', 'New York') # Brandon instance
brandon.describe_user()
brandon.greet_user()



