# page 146 8.9
def show_messages(messages):
    """
    Make a list containing a series of short text messages. 
    Pass the list to a function called show_messages(), which prints each text message
    """
    for message in messages:
        print(message)
    
messages = ['Hello this is a message!', 'this is a second message!']

show_messages(messages)