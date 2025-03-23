# Page 111 
# 6.12

cities = {
    'new york city': {
        'state': 'new york',
        'region': 'north east',
        'population': '8250000',
        'year founded': '1624',

    },
    'chicago': {
        'state': 'illinois',
        'region': 'midwest',
        'population': '2600000',
        'year founded': '1837',
    },
    'los angeles': {
        'state': 'california',
        'region': 'west',
        'population': '3820000',
        'year founded': '1781',
    }

}

for city, city_info in cities.items(): # assign variables - city and city_info
    
    state = f'{city_info['state'].title()}' # create a new variable that prints the state 
    region = f'{city_info['region'].title()}' # create a new variable that prints the region
    population = f'{city_info['population'].title()}' # Create population 
    year_founded = f'{city_info['year founded'].title()}' # create year founded
    city_information = f'\nCity Information for {city.title()}:\nState: {state}\nRegion: {region}\nPopulation: {population}\nYear Founded: {year_founded}' # Create a variable that puts it all together
    
    print(city_information)
