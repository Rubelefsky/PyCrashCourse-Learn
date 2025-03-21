# Create dictionary with 2 keys. Aeinstein and mcurie
# Value associated with each key is a dictionary that includes, first, last and location
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items(): # assigns username to key and userinfo to value
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}" # Assign full_name variable to first and last from user_info variable
    location = user_info['location'] # assign location variable to user location

    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")