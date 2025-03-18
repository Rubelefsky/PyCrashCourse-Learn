# Page 106

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(100): # Returns a series of numbers, which tells Python how many times we want the loop to repeat
    new_alien = {'color': 'green', 'points': '5'} # Each time the loop is ran, we want a new alien to be created
    aliens.append(new_alien) # after creating the new alien - append to the list **aliens**

# Show the first 5 aliens
for alien in aliens[:5]: # use slice to print the first five aliens
    print(alien)
print("...")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")