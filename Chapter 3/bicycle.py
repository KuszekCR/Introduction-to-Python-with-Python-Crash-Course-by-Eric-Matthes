### LIST ###

''' A list is a collection of items in a particular order. You can make a list that 
includes the letters of the alphabet, the digits from 0–9, or the names of 
all the people in your family. You can put anything you want into a list, and 
the items in your list don’t have to be related in any particular way. Because 
a list usually contains more than one element, it’s a good idea to make the 
name of your list plural, such as letters, digits, or names. 
In Python, square brackets ([]) indicate a list, and individual elements 
in the list are separated by commas. '''

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bicycles)

### ACCESING ELEMENTS IN A LIST ### 

''' Lists are ordered collections, so you can access any element in a list by 
telling Python the position, or index, of the item desired. '''

#print(bicycles[0].title()) # We can add more functions into these elements, such as TITLE and apply it to an element of the list
#print(bicycles[3])

### VERY IMPORTANT ###

''' Python considers the first item in a list to be at position 0, not position 1. 
This is true of most programming languages, and the reason has to do with 
how the list operations are implemented at a lower level. If you’re receiving 
unexpected results, determine whether you are making a simple off-by-one 
error. 
Also, Python has a special syntax for accessing the last element in a list. By 
asking for the item at index -1, Python always returns the last item in the list'''

#print(bicycles[-1]) # It´ll return the last item on the list.
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)