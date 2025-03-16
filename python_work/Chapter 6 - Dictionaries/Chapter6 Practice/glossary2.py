# 6.4 
# Using https://devdocs.io/python~3.13/glossary#term-dictionary for definitions

glossary = {
    'variable': 'a named storage location that holds a value', 
    'loop': 'control flow structure that allows a block of code to be executed repeatedly',
    'if-else': 'conditional true false',
    'list': 'store multiple items in a variable',
    'tuple': 'immutable list',
    'set': 'unique',
    'dictionary': 'An associative array'
    }

for term, definition in glossary.items(): # assigned term to key and definition to value
    print(f'A {term.title()} is defined as {definition}.') # Grammar is not the best but the loop works
