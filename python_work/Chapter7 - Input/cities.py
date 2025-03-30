# Page 121
#Create prompt
prompt = "\nPlease enter the name of a city you have visited:" 
prompt += "\n(Enter 'quit' when you are finished.)"

while True: 
    city = input(prompt)

    if city == 'quit': # If quit is input
        break # break the loop if quit is input
    else:
        print(f"I'd love to go to {city.title()}!") 
        # else print above