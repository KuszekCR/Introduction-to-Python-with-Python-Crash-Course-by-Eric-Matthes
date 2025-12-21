### TUPLES ###

''' Lists work well for storing collections of items that can change throughout 
the life of a program. The ability to modify lists is particularly important 
when you’re working with a list of users on a website or a list of characters in 
a game. However, sometimes you’ll want to create a list of items that cannot 
change. Tuples allow you to do just that. Python refers to values that cannot 
change as immutable, and an immutable list is called a tuple.'''

#dimensions = (200, 50)
#print(dimensions[0])
#print(dimensions[1])

#dimensions[0] = 250
#print(dimensions[0])
# 'tuple' object does not support item assignment is the error that the program is gonna show
''' This is beneficial because we want Python to raise an error when a line 
of code tries to change the dimensions of something established, something that it
isn´t recommended to change.'''

### Looping Through All Values in a Tuple ###

'''You can loop over all the values in a tuple using a for loop.'''

#for dimension in dimensions:
#    print(dimension) #Python returns all the elements in the tuple, just as it would for a list.

### Writing over a Tuple ###
'''Although you can’t modify a tuple, you can assign a new value to a variable 
that represents a tuple. So if we wanted to change our dimensions, we could 
redefine the entire tuple. '''

dimensions = (200, 50)
print("Original Dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified Dimensions:")
for dimension in dimensions:
    print(dimension)

'''Python doesn’t raise any errors this 
time, because reassigning a variable is valid.'''

'''When compared with lists, tuples are simple data structures. Use them 
when you want to store a set of values that should not be changed through
out the life of a program.'''

