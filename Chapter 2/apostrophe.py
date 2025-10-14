### AVOIDING SYNTAX ERRORS WITH STRINGS ###

''' One kind of error that you might see with some regularity is a syntax error. 
A syntax error occurs when Python doesn’t recognize a section of your program 
as valid Python code. For example, if you use an apostrophe within 
single quotes, you’ll produce an error. This happens because Python interprets 
everything between the first single quote and the apostrophe as a 
string. It then tries to interpret the rest of the text as Python code, which 
causes errors.'''

#message = "One of Python's strengths is its diverse community."
#print(message)

''' Here we have no problem since the apostrophe in Python´s is simple, not double as we see at 
the beginning and at the end of the string.'''

#new_message = 'One of Python's strengths is its diverse community.'
#print(new_message)

# It´ll throw the next SyntaxError: unterminated string literal (detected at line 17)

print("Albert Einstein once said, “A person who never made a mistake never tried anything new.”")
famous_person = "Albert Einstein"
