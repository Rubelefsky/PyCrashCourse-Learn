# Page 103
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()): # tells python to get all keys sorted in the dictionary
    print(f'{name.title()}, thank you for taking the poll.')