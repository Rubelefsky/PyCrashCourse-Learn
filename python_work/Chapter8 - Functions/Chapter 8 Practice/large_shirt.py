# page 136 8.4

def make_shirt(size='large', message='I love Python!'): # Create function
    """Create make shirt with a default value"""
    print(f"\nI am going to make a {size} t-shirt.")
    print(f"It will say, {message}")

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')
