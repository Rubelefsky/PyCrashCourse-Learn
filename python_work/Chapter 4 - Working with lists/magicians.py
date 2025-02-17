# Looping through an entire list
magicians = ['Carol', 'John', 'Jose'] # create list
for magician in magicians: # loop through all magicians in magicians. For every magician in the list of magicians, print the magicians name.
    print(magician) # Prints the list


cats = ['Jerry', 'Paulie', 'Sandy']
for cat in cats:
    print(f"{cat.title()} is very cuddly!") # Every indented line is considered in the loop.
    print(f"I wonder if {cat.title()} will hunt for mice.\n") # The newline at the end will make everything more neat. 

print("Even though I am a dog person, those cats were cute.") # Not indented so not in the loop

    