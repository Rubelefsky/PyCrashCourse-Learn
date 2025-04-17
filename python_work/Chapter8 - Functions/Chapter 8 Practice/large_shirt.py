# page 136 8.4

def make_shirt(size, message): # Create function
    """Create make shirt with a default value"""
    print(f"\nI am going to make a {size} t-shirt.")
    print(f"It will say, {message}")

make_shirt('large', 'I love python!')
make_shirt(message="Readability counts.", size='medium')