# 7.5 
age = int(input("What is your age? ")) # Create an age variable. Wrap the input in int()
# Same thing as age = int(age)

if age < 3: # if age less than 3
    print(f"Your ticket is free.") 
elif age > 3 and age < 12: # If age more than 3 and less than 12
    print("Your ticket is $10.")
else: 
    print("Your ticket is $15.")