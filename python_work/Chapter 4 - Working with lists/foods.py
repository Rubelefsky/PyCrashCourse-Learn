# Copying a list
my_foods = ['pizza', 'falafel', 'hamburgers', 'bagel'] # Create a list of favorite foods
friend_foods = my_foods[:] # Make a copy of my_foods list and create a variable friend_foods/lists, no specifying indexes

print("My favorite foods are:")
print(my_foods) # Pring List

my_foods.append('cannoli') # add cannoli to the end of my_foods list
friend_foods.append('ice cream') # add ice cream to the end of friend_foods list

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)


