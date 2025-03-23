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

for city, city_info in cities.items(): # assign variables - city and city_info
    
    state = f'{city_info['state'].title()}' # create a new variable that prints the state 
    region = f'{city_info['region'].title()}' # create a new variable that prints the region
    city_information = f'\nCity Information for {city.title()}:\nState: {state}\nRegion: {region}' # Create a variable that puts it all together
    
    print(city_information)