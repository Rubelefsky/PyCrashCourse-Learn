alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points']) # Key Error

point_value = alien_0.get('points', 'No point value assigned.') # get() sets default value that will be returned if the requested key does not exist.
print(point_value)