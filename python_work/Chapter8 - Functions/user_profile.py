# Page 148

def build_profile(first, last, **user_info): # Expects a first and last name, and allows user to pass in as many name-value pairs as wanted
    # The ** before parameter creates a dictionary called user_info containing all the extra name-value pairs the function recieves.
    """Build a dictionary containing everything we know about a user""" 
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info # Return the user_info dictionary to the function call line.

user_profile = build_profile('albert', 'einstein', location ='princeton', field='physics') # Function will work no matter how many additional key-value pairs are provided in the function call.

print(user_profile)
