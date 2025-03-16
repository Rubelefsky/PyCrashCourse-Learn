# Page 101
# Create a dictionary named favorite_languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
# Looping through keys is the default behaivor when looping through a dictionary
for name in favorite_languages.keys(): # Can change to values() as well for python, rust, c etc
    print(name.title())