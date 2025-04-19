# page 138


def get_formatted_name(first_name, last_name, middle_name=''): # set default value of middle_name to to ignore argument unless user provides a value
    """
    Return a full name, neatly formatted.
    """
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('bob', 'dylan')
print(musician) 

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)