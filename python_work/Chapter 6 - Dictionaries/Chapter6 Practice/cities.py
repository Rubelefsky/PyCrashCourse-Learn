# Page 111 6.10
# Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city.

cities = {
    'new york city': {
        'state': 'new york',
        'region': 'north east',

    },
    'chicago': {
        'state': 'illinois',
        'region': 'midwest',
    },
    'los angeles': {
        'state': 'california',
        'region': 'west',
    }

}

for city, city_info in cities.items():
    print(city.title())
    print(city_info)