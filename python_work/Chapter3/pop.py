# Remove items using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycles = motorcycles.pop() # Removes last item in the list and assigns it to Variable popped_motorcycles
print(motorcycles)
print(popped_motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# Popping from any position in the list
motorcycles_new = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles_new.pop(0) # Pops the 0 position and assigns it to first_owned.

print(f"The first motorcycle I owned was a {first_owned.title()}.")

