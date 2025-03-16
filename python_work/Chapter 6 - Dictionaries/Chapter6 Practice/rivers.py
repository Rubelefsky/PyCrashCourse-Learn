# 6.5 Make a dictionary containing three major rivers and the country each river runs through. 
# One key-value pair might be 'nile': 'egypt'


# Create a dictionary called rivers
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "congo": "drc",
}

for river, country in rivers.items():
    print(f'\nThe {river.title()} runs through {country.title()}.')
    print(f'{river.title()}')
    print(f'{country.title()}')


