# Page 118

# first define a prompt that tells the user their two options
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

# setup variable to keep track of whatever value is entered
message = "" # define message as an empty string
while message != 'quit': #
    message = input(prompt)
    print(message)

    if message != 'quit': # Now the program makes a quick check before displaying the message and only prints the message if it does not match the quit value.
        print(message)

# taken from Page 119 in python crash course 3rd edition

# The first time through the loop, message is just an empty string, so Python enters the loop. 
# At message = input(prompt), Python displays the prompt and waits for the user to enter their input. Whatever they enter is assigned to message and printed; then, Python reevaluates the condition in the while statement. 
# As long as the user has not entered the word 'quit', the prompt is displayed again and Python waits for more input. 
# When the user finally enters 'quit', Python stops executing the while loop and the program ends: