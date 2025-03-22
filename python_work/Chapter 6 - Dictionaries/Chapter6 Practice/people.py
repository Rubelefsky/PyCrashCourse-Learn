# Start with the program you wrote for Exercise 6-1 (page 98). Make two new dictionaries representing different people, and store all three dictionar- ies in a list called people. 
# Loop through your list of people. 
# As you loop through the list, print everything you know about each person.
people = {
    'brubell': {
        'first_name': 'brandon', 
        'last_name': 'scott', 
        'age': '32', 
        'city': 'new york',
    },
}

for person, person_info in people.items():
    print(f"Person: {person.title()}")
    full_name = f"{person_info['first_name']} {person_info['last_name']}"
    print(f"{full_name.title()}")

