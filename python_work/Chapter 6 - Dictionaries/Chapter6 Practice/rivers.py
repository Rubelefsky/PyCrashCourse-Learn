# 6.5 Make a dictionary containing three major rivers and the country each river runs through. 
# One key-value pair might be 'nile': 'egypt'


# Create a dictionary called rivers
rivers = {
    "nile": "egypt",
    "amazon": "brazil",
    "congo": "drc",
}

print(rivers)
for river in rivers:
    print(f"This called the {river.title()} river.")
