# Page 117 7.3

answer = input("Choose a number: ") # Create variable called answer
answer = int(answer) # Convert answer to int

if answer % 10 == 0: # Checks if answer % 10 is equal to 0
    print(f"{answer} is a multiple of 10")
else:
    print(f"{answer} is not a multiple of 10")