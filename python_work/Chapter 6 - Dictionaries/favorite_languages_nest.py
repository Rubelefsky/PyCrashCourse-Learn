# Page 109

# Create dictionary
favorite_languages = { 
    'jen': ['python', 'rust'],
    'sarah': ['c'], 
    'edward': ['rust', 'go'], 
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items(): # name and languages are key / value
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages: # use a second loop run through languages of each person
        print(f"\t{language.title()}")