# 154 Chapter 8 TRY IT YOURSELF 8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. 
# Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.

import printing_functions

unprinted_designs = ['iphone case', 'lego car']
completed_models = []

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)