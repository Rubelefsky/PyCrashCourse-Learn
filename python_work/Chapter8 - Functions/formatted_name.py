# page 137
# Return values - A function doesn’t always have to display its output directly. 
# Instead, it can process some data and then return a value or set of values. 
# The value the function returns is called a return value.


def get_formatted_name(first_name, last_name): # first and last name parameters
    """
    Args:
        first_name (_type_): _description_
        last_name (_type_): _description_
    """
    full_name = f"{first_name} {last_name}" # function combines two names, and assigns results to full_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix') # when calling a function that returns a value, need to provide a variable that the return value can be assigned to.
print(musician)