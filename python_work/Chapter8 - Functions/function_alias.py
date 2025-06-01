# If the name of function conflicts with an existing name in your program
# Or if function is to long, can use an alias
# An alternate name similar ot a nickname for the function

from pizza import make_pizza as mp # alias is mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# General syntax for providing an alias:
# import module_name as mn
