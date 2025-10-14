### F-STRINGS ###

''' In some situations, you’ll want to use a variable’s value inside a string. For 
example, you might want two variables to represent a first name and a last 
name respectively, and then want to combine those values to display some
one’s full name.'''

first_name = "rodrigo"
last_name = "kuszek"
full_name = f"{first_name} {last_name}"
#print(full_name.title())

''' These strings are called f- strings. The f is for format, because Python 
formats the string by replacing the name of any variable in braces with its 
value.'''

''' You can also use f- strings to compose a message, and then assign the 
entire message to a variable.'''

message = f"Hello, {full_name.title()}, how are you?"
#print(message)

### WHITESPACES ###

''' In programming, whitespace refers to any nonprinting character, such as 
spaces, tabs, and end- of- line symbols. You can use whitespace to organize 
your output so it’s easier for users to read.'''

#print("Python")
#print("\tPython")

''' To add a newline in a string, use the character combination \n:'''

#print("Languages:\nPython\nC\nJavaScript")

''' You can also combine tabs and newlines in a single string. The string 
"\n\t" tells Python to move to a new line, and start the next line with a tab. '''

print("Languages:\n\tPython\n\tC\n\tJavaScript")

