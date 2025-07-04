# Make function from printing_models.py
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop() # pop items from unprinted designs
        print(f"Printing models: {current_design}")
        completed_models.append(current_design) # add to completed models from current design

def show_completed_models(completed_models):
    """Show all models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models: # loop through list completed_models
        print(completed_model)

        