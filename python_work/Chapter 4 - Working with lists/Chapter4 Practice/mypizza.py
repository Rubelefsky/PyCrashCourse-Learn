# 4.11
my_pizza = ['cheese', 'chicken', 'pasta slice', 'margharita'] # Create a list of my_pizza
friends_pizza = my_pizza[:] # Copy list of my_pizza to friends_pizza

friends_pizza.append('sausage') # Append sausage
print(friends_pizza) # print appended list

print("My favorite pizzas are:")
for pizza in my_pizza:
    print(pizza.title())

print("\nMy friends favorite pizzas are:")
for pizza in friends_pizza:
    print(pizza.title())

