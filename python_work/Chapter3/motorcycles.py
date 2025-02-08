motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Modifying
motorcycles[0] = 'ducati' # Modifies the 0 position
print(motorcycles)

# Adding
motorcycles.append('honda') # Adds Honda to the end of the list
print(motorcycles)

# Adding to the list
motorcycles_new = []

motorcycles_new.append('honda')
motorcycles_new.append('ducati')
motorcycles_new.append('BMW')
motorcycles_new.append('suzuki')

print(motorcycles_new)

# Inserting into lists
motorcycles_new.insert(0, 'Harley') # Insert Harley into the 0 position
print(motorcycles_new)


# Removing From List using del statement
del motorcycles_new[0] # Removes the value from the 0 position
print(motorcycles_new)

del motorcycles_new [1] # Removes the value from the 1 position
print(motorcycles_new)

