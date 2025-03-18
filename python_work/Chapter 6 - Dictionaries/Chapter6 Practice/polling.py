# 6.6 
favorite_languages = { 
  'jen': 'python', 
  'sarah': 'c', 
  'edward': 'rust', 
  'phil': 'python',
  'rick': 'java'
}

polling_list = ['jen', 'brandon', 'phil', 'sarah'] # list

# Can use favorite_languages.keys() for easier readability. favorite_languages defaults to keys 
for name in favorite_languages.keys(): # Pull all keys from dictionary and assign them one at a time to variable "name"
    print(f"Hello {name.title()}, you are in the favorite languages dictionary.")

    if name in polling_list: # 
        polling_name = favorite_languages[name].title()
        print(f"\t{name.title()}, you are in the polling list as well.")

    else:
        print(f"\t{name.title()}, you are not in the polling list.")

        
        


