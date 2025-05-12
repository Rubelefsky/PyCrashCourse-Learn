# Page 146
# 8.10

def show_messages(messages):    # Function called show_messages
    """
   Start with a copy of your program from Exercise 8-9. 
   Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
   After calling the function, print both of your lists to make sure the messages were moved correctly.
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
send_messages(messages, sent_messages) # calls function send_messages, Removes each message from messages, prints each message, adds each messages to sent_messages

print("\nFinal lists:") # print Final Lists:
print(messages) # prints messages list (now empty)
print(sent_messages) # prints sent_messages list