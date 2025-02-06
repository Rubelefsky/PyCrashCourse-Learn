bicycles = ['trek', 'cannondale', 'fiji', 'giant', 'specialized']
print(bicycles)
print(bicycles[0]) # Index positions start at 0
print(bicycles[1])
print(bicycles[0].title())
print(bicycles[-1]) # Accesses the last item in the list

first_bike = f"My first bike was a {bicycles[0].title()}."
print(first_bike)


current_bike = f"My current bike is a {bicycles[3].title()}."
print(current_bike)