# 3.6 More Guest = Page 42

guest_list = ['Joe', 'Steve', 'Mike', 'Dan']
print(guest_list)

guest_list.insert(0, 'Jack')
print(guest_list)

guest_list.insert(3, 'John')
print(guest_list)

guest_list.append('Joel')
print(guest_list)

invitation_jack = f"Please save the date, {guest_list[0].title()}."
print(invitation_jack)