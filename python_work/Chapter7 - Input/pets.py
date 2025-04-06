pets = ['dog', 'cat', 'goldfish', 'cat' , 'rabbit', 'cat'] # Create a list with multiple instances of cat
print(pets)

while 'cat' in pets: 
    pets.remove('cat') # Loops through and removes each instance it finds and once it is not longer in the list prints

print(pets)