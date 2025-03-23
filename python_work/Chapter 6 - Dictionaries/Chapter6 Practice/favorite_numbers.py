favorite_numbers = { # Create dictionary
    'carol': [23, 42], 
    'brandon': [29, 78], 
    'steve': [14, 65], 
    'jerry': [49, 90], 
    'scott': [46, 2]
}

print(favorite_numbers['carol']) # test print to see that both numbers print



for name, numbers in favorite_numbers.items(): # assign variable name and numbers to key-value
    print(f"\n{name.title()}'s favorite numbers are {numbers}.")