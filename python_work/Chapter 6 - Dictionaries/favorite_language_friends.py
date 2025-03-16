# Page 102
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['phil', 'sarah']
for name in favorite_languages.keys(): # Loop through names in dictionary
    print(f"Hi {name.title()}.") 

    if name in friends: # Check if name is in friends list above
        language = favorite_languages[name].title() # IF  name is in list, determine the favorite language using the name of the dictionary (favorite_languages) and current value of name as the key (name)
        print(f"\t{name.title()}, I see you love {language}!") # print special greeting

    if 'erin' not in favorite_languages.keys(): # Checks if name erin is in dictionary. If it is not - then it prints below
        print('Erin, please take our poll!')