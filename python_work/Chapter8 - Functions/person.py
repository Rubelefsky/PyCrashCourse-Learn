# page 138

# Returning a dictionary
def build_person(first_name, last_name, age=None): # none is a placeholder value. None evaluates to False in conditional tests.
    """
    Return a dictionary of information about a person.
    """
    person = {'first': first_name, 'last': last_name}# values are stored as a dictionary
    if age:
        person['age'] = age
    return person # entire dictionary represeneting the person is returned

musician = build_person('jimi', 'hendrix', age=27)
print(musician)