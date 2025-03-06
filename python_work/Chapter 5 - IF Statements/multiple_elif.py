age = 66

if age < 4: # IF age less than 4
    price = 0 # Price is 0
elif age < 18: # IF age less than 18 
    price = 25 # Price is 25
elif age < 65: # IF age less than 65
    price = 40 # Price is 40
else: # ELSE -Statement is the catchall.Matches any condition that was not matched by a specific IF or ELIF test
    price = 20 # Price is 20

print(f"Your admission price cost is {price}.")