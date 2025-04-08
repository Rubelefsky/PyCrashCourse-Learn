# Page 127 7.8

# Make a list called sandwich_orders / Fill with Various sandwiches
sandwich_orders = ['BLT', 'Turkey Ranch', 'Roast Beef Hero', 'Chicken Parm']

# Create an empty list called finished_sandwiches
finished_sandwiches = []


while sandwich_orders: # While there are sandwiches in this list...
    sandwich = sandwich_orders.pop() # remove sandwiches from sandwich order list / assign to variable sandwich

    print(f"I am now making a {sandwich} sandwich.")
    finished_sandwiches.append(sandwich) # add the sandwich to the finished sandwiches list

print(f"\nThese sandwiches have been made:")
for finished_sandwich in finished_sandwiches: # loop through now filled list
    print(f"{finished_sandwich.title()}") # print finished sandwiches in list

