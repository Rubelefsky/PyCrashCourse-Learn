age = 15
if age < 4:
    print("Your admission cost is $0.") # If age is below 4 print $0
elif age < 18: # Only runs if previous test fails 
    print("Your admission cost is $25.") # Between ages of 4 and 18 print $25
else:
    print("Your admission cost is $40.") # Over 18 print $40
