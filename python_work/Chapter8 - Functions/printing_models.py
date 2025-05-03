# Start with designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = [] # create empty list

# Simulate printing each design, until none are left.
# Mode each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop() # pop items from unprinted designs
    print(f"Printing models: {current_design}")
    completed_models.append(current_design) # add 

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models: # loop through list completed_models
    print(completed_model)