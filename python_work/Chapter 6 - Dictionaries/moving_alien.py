alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} # Create dictionary
print(f'Original position: {alien_0['x_position']}') # Print Original Position: 0

# Move the alien to the right
# Determine how far to move the based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: # Fast Alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New Position: {alien_0['x_position']}") # Speed of Alien is medium so +2 increment
