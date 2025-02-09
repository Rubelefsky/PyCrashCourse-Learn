# 3.5 Changing Guest List - Page 42

guest_list = ['scott', 'brandon', 'steven', 'russ']
print(guest_list)


print(f"Here is the guest list. \n{guest_list[0].title()}\n{guest_list[1].title()}\n{guest_list[2].title()}\n{guest_list[3].title()}")

leaving_guest = 'scott'
guest_list.remove(leaving_guest)

print(leaving_guest)

leaving_guest_message = f"{leaving_guest.title()} will not be joining us tonight."
print(leaving_guest_message)


