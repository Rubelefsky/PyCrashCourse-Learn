def get_formatted_name(first_name, last_name):
    """
    Return a full name, neatly formatted.
    """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop
while True:
    print(f"\nPlease tell me your name.")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break
# if q is entered in first or last name the program quits
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
