# Tuples are lists that are immutable. Immutable = values that cannot change.
# Tuples use Parentheses () instead of Square [] brackets

dimensions = (200, 50) # create tuple called dimension
print(dimensions[0]) # Print first item in tuple - 200
print(dimensions[1]) # Print second item in tuple - 50

# dimensions[0] = 250 | would not work as you cannot alter a tuple
# This will raise an error "Tuple does not support item assignment"
