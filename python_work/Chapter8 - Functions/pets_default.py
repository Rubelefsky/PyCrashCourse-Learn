# page 134

# When writing a function, you can define a default value for each parameter
def descibe_pet(pet_name, animal_type='dog'):
    """Display information about a pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

descibe_pet(pet_name='willie')

# When using default values, any parameter with a default value needs to be listed after all the parameters that don't have default values.
# This allows python to continue interpreting positional arguments correctly.