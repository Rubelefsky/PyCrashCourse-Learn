import module_import # import the name of the file that is the function
# When Python reads this file, the line import module_import tells Python to open the file module_import.py and copy all the functions from it into this program. 

# To call a function from an imported module, enter the name of the module you imported, module_import, followed by the name of the function, make_pizza(), separated by a dot
# This code 
module_import.make_pizza(16, 'pepperoni')
module_import.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

