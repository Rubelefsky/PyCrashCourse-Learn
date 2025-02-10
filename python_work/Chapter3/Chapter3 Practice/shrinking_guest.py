# 3.7 Shrinking Guest List - Page 42
guest_list = ['Joe', 'Steve', 'Mike', 'Dan']
message = 'Only 2 people can make it tonight.'

print(message)

guest_1 = guest_list.pop(0) # Assigns guest 1 to Joe
guest_2 = guest_list.pop(1) # Assigns guest 2 to Steve

print(guest_1)
print(guest_2)

new_message = f"{guest_1.title()} and {guest_2.title()} will be joining us for dinner tonight."
print(new_message)

print(guest_list)

del guest_list[0]
del guest_list[0]

print(guest_list)