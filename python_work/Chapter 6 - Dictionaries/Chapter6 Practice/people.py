# Start with the program you wrote for Exercise 6-1 (page 98). Make two new dictionaries representing different people, and store all three dictionar- ies in a list called people. 
# Loop through your list of people. 
# As you loop through the list, print everything you know about each person.
people = {
    'brubell': {
        'first_name': 'brandon', 
        'last_name': 'scott', 
        'age': '32', 
        'city': 'manhattan',
    },
    'adaniels': {
        'first_name': 'adam', 
        'last_name': 'daniels', 
        'age': '28', 
        'city': 'brooklyn',
    }
}

people_list = [people['brubell'], people['adaniels']]

for person, person_info in people.items(): # assign key/value variables - person and person_info
    full_name = f"{person_info['first_name']} {person_info['last_name']}"
    age = f'{person_info['age']}'
    city = f'{person_info['city']}'
    
    print(f"\nPerson: {person.title()}")
    print(f"Full Name: {full_name.title()}")
    print(f"Age: {age}")
    print(f"City: {city.title()}")


print(f"\n{people_list[0]}")