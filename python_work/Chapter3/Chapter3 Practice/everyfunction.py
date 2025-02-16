# 3.10 Make a list and use every function

cars = ['porsche', 'toyota', 'honda'] # List named cars
print(cars)

favorite_car = cars[0] # Assign variable to the 0 spot in the cars list. Will be Porsche.
print(favorite_car.title()) # Prints and makes the p capital

message = f'My favorite car is a {favorite_car.title()}.' # Creates a variable called message which will print the message with the f.
print(message)

lastonlist = cars.pop() # Create a variable that assigns the pop function
print(lastonlist) # Print the last item on the list that was popped out
print(cars) # Prints new list with Honda removed

cars.append('BMW') # Adds BMW to the last spot on the list
print(cars)

length = len(cars) # Assigns variable length of list
print(length) # Prints length with is 3

cars.reverse() # Reverses List
print(cars) # Prints reverse list

print("\nThis will be the sorted list") # Sorts the list by alphabetical order temporarily
print(sorted(cars))

print(cars)

cars.sort() # permnanently change the list to sort
print(cars)

cars.sort(reverse=True) # Permanently changes the list to be sorted in reverse
print(cars)

cars.remove('BMW') # Removed BMW from the list
print(cars)

reliable_car = 'toyota' # creates a a variable named reliable car
cars.remove(reliable_car) # Removes toyota as it is assigned the variable
print(cars) # prints new list
print(reliable_car.title()) # Prints reliable_car variable
print(f"{reliable_car.title()} is very reliable.") # Prints toyota is very reliable.