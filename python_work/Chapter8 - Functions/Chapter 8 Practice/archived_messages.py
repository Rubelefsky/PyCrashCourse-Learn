# 8.11 
def show_messages(messages):    # Function called show_messages
    """
Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 
After calling the func- tion, print both of your lists to show that the original list has retained its messages.
    """
    print("Showing all messages:") # Prints showing all messages
    for message in messages: # loop through each message in messages
        print(message) # print each message without modifying the list

def send_messages(messages, sent_messages): # 2 parameters, messages list and empty list
    """Print each message and move it to sent_messages"""
    print("\nSending all messages:") # print Sending all messages:
    while messages: # While loop that continues while items are in the list
        current_message = messages.pop() # create variable current_message and pop() from messages list
        print(current_message) # print the removed messaged
        sent_messages.append(current_message) # append messages to sent_messages list


messages = ["Hello, how are you?", "This is a python function"] # list called messages
show_messages(messages) # calls function show_messages with messages list

sent_messages = [] # empty list called sent_messages
send_messages(messages[:], sent_messages) # calls function send_messages, uses a copy of messages and does not remove from the original list.

print("\nFinal lists:") # print Final Lists:
print(messages) # prints messages list (full as a copy was called in the function)
print(sent_messages) # prints sent_messages list
