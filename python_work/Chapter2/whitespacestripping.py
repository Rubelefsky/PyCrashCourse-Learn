print("Python")
print("\tPython") # \t = tab
print("Languages:\nPython\nC\nJavascript") # \n = new line
print("Languages:\n\tPython\n\tC\n\tJavascript") # \n\t = new line and tab


# Stripping Whitespace
favorite_language = "python "
print(favorite_language)
print(favorite_language.rstrip()) # rstrip() = right strip
favorite_language = favorite_language.rstrip() # reassigns variable with rstrip
print(favorite_language)

language = " python "
right_strip = language.rstrip() # right strip
left_strip = language.lstrip() # left strip
full_strip = language.strip() # full strip
print(full_strip)