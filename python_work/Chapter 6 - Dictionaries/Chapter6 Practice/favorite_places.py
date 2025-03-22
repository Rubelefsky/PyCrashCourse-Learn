# 6.9 

favorite_places = {
    'brandon': {
        'location': 'italy',
    },
    'steve': {
        'location': 'paris'
    },
    'russ': {
        'location': 'aruba'
    }
}

for name, favorite_spots in favorite_places.items():
    
    print(f'\n{name.title()}')
    print(f'Favorite Spot:{favorite_spots['location'].title()}')