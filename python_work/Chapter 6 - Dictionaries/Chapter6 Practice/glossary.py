# 6.3 Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values.

glossary = {
    'variable': 'a named storage location that holds a value', 
    'loop': 'control flow structure that allows a block of code to be executed repeatedly',
    'if-else': 'conditional true false',
    'list': 'store multiple items in a variable',
    'tuple': 'immutable list'
    }

for word in glossary: # For word in glossary dictionary
    if word == 'variable': # IF the word is == variable, print below.
        print('\nA variable test loop and if statement.')


print(f"\nA variable is {glossary['variable']}.")
print(f"\nA loop is a {glossary['loop']}.")
print(f"\nAn if-else is {glossary['if-else']}.")

