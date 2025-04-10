# Page 126 7.9
sandwich_orders = ['BLT', 'pastrami', 'Turkey Ranch', 'Roast Beef Hero', 'pastrami', 'Chicken Parm', 'pastrami'] # using list from 7.8, adding pastrami 3 times

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    
finished_sandwiches = sandwich_orders

print(f"Here are the finished sandwiches: \n{finished_sandwiches}")

