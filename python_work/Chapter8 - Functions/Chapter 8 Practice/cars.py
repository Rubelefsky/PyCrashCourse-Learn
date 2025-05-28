# Page 149
def build_car(manufacturer, model, **kwargs): # kwargs = key word arguments
    """
    Write a function that stores information about a car in a diction- ary. 
    The function should always receive a manufacturer and a model name. 
    It should then accept an arbitrary number of keyword arguments. 
    Call the func- tion with the required information and two other name-value pairs, such as a color or an optional feature. 
    Your function should work for a call like this one:
    """
    kwargs['car_manufacturer'] = manufacturer
    kwargs['car_model'] = model
    return kwargs # Returns the kwargs dictionary, now containing the manufacturer, model, and any other keyword arguments provided.

new_car = build_car('honda', 'accord', car_color='gray', seat_type='leather')
print(new_car)