favorite_places = {} # Empty dictionary

# Create a poll for favorite places to visit.
polling_active = True

while polling_active:
    # prompt for name and where favorite place is
    name = input("\nWhat is your name?")
    response = input("What is your favorite place in the world?")
    
    favorite_places[name] = response
    
    repeat = input("Would you like someone else to respond? (yes /no)")
    if repeat == 'no':
        polling_active = False
        
    print("\n--- Dream Vacations ---")
    for name, response in favorite_places.items():
        print(f"{name.title()} dream vacation spot is {response.title()}.")

    