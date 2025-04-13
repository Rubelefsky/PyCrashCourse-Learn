def describe_pet(animal_type, pet_name): # define function with positional arguments
    # positional arguments - need to be in the same order the parameters were written
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')