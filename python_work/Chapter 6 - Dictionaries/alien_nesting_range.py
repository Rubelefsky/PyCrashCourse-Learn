# Page 106

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(100): # Returns a series of numbers, which tells Python how many times we want the loop to repeat
    new_alien = {'color': 'green', 'points': '5'} # Each time the loop is ran, we want a new alien to be created
    aliens.append(new_alien) # after creating the new alien - append to the list **aliens**

for alien in aliens[:3]: # Modify the first 3 aliens
    if alien['color'] == 'green': # If equal to green # Page 106/107
        alien['color'] = 'yellow' # assign new color - yellow
        alien['speed'] = 'medium' # assign new speed - medium
        alien['points'] = 10 # assign new point value - 10
    elif alien['color'] == 'yellow': # IF equal to yellow
        alien['color'] = 'red' # assign new color - red
        alien['speed'] = 'fast' # assign new speed - fast
        alien['points'] = 15 # assign new point value - 
        15

# Show the first 5 aliens
for alien in aliens[:5]: # use slice to print the first five aliens
    print(alien)
print("...")

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")