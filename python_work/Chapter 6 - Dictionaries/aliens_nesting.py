# Page 105
# Create multiple dictionaries
alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}

# Create a list with the dictionaries
# This is called nesting
# You can nest dictionar- ies inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.
aliens = [alien_0, alien_1, alien_2]


for alien in aliens:
    print(alien)
