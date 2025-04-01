# 7.4 

toppings_list = [] # Create an empty list

toppings = input('What are your favorite toppings? ') # create input
print(toppings) # print input

toppings_list.append(toppings) # append toppings to toppings_list
print(toppings_list) # print list to test

print(f"You have added the following toppings to your pizza. {toppings_list}")