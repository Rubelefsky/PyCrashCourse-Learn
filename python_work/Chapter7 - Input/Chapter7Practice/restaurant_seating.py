# Page 117 - 7.2

seating_number = input("How many people will be dining tonight? ") # Create variable with input
number = int(seating_number) # Create a new var and change the string to integer

if number >= 8: # if the input is greater than or equal to 8
    print("You will need to wait for a table.") # print if >=
else: # Else print
    print("Your table is ready!")