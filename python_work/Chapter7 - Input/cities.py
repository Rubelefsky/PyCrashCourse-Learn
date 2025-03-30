# Page 121
#Create prompt
prompt = "\nPlease enter the name of a city you have visited:" 
prompt += "\n(Enter 'quit' when you are finished.)"

while True: 
    city = input(prompt)

    if city == 'quit': # If quit is input
        break # break the loop if quit is input - use break to exit a while loop
    else:
        print(f"I'd love to go to {city.title()}!") 
        # else print above

        # a loop with a TRUE statement will run forever unless it reaches a break statement.
        # Can use the break statement in a python loop
        
