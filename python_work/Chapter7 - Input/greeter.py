#  Page  114
prompt = "If you share your name, we can personalize the messages you see."
prompt +=  "\nWhat is your first name? " # the += takes the string that was assigned to prompt and adds the new string onto the end.

name = input(prompt)

print(f"Hello, {name.title()}!")
