# Slicing a list - Specify the first and last elements that you want to work with
players = ['steven', 'zoe', 'smithy', 'blidy', 'blouy'] # Creates a list named players
print(players[0:3]) # Prints first 3 in the list
print(players[1:4]) # Prints Zoe, smithy, blidy
print(players[:3]) # Omitting the first index will automatically start it at the beginning
print(players[3:]) # Omitting the second index will include the end of the list
print(players[-3:]) # Prints the last 3 on the list

print("Here are the first three players on my team:")
for player in players[:3]: # loops through first three players
    print(player.title()) # prints players with first letter capital