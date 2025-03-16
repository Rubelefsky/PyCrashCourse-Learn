# Page 104

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): # a **set** is a collection in which each item must be unique.
    print(language.title())

# When wrapping set() around a collection of values that contains duplicate items, Python identifies the unique items in the collection and builds a set from those items.