# Page 146
# 8.10

def show_messages(messages):    # Function called show_messages
    """
   Start with a copy of your program from Exercise 8-9. 
   Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed. 
   After calling the function, print both of your lists to make sure the messages were moved correctly.
    """
    print("Showing all messages:")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages"""
    print("\nSending all messages:")
    while messages:
        current_message = messages.pop() 
        print(current_message)
        sent_messages.append(current_message)

messages = ["Hello, how are you?", "This is a python function"]
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)