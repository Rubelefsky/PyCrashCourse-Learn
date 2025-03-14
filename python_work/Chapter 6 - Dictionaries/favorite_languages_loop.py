# page 100
# Create a dictionary named favorite_languages
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items(): # Name is assigned to the Key / Language is assinged to the Value
    print(f"{name.title()}'s favorite language is {language.title()}.") # print name(key) and language(value)