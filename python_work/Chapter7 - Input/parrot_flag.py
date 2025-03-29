# Page 120

# first define a prompt that tells the user their two options
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."


# For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the entire program is active.
# This variable, called a flag, acts as a signal to the program. 
# We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False.

active = True # set active to true so program starts in active state
while active: # as long as the active variable remains true, the loop will continue running
    message = input(prompt)

    if message == 'quit': # Check value of the message. If the user enters quit, the active value gets set to False
        active = False
    else: # if the user enters anything other than quit - the message is printed
        print(message)

