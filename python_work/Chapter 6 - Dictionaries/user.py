# Looping through all Key-Value Pairs
# Page 99
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_0.items(): # key and value select each respective Key and Value item1, item2. items() is a method - returns a sequence of key=value pairs
    print(f"\nKey {key}") # Prints the key value (username, first, last)
    print(f"Value: {value}") # Prints the value, value (efermi, enrico, fermi)

# Can use abbreviations as well
# for k, v in users_0.items()



