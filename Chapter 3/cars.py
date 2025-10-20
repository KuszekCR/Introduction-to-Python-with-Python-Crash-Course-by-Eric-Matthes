### ORGANIZING A LIST ###

'''Often, your lists will be created in an unpredictable order, because you can’t 
always control the order in which your users provide their data. Although 
this is unavoidable in most circumstances, you’ll frequently want to present 
your information in a particular order. Sometimes you’ll want to preserve the 
original order of your list, and other times you’ll want to change the original
order. Python provides a number of different ways to organize your lists, 
depending on the situation.'''

'''Python’s sort() method makes it relatively easy to sort a list. Imagine we 
have a list of cars and want to change the order of the list to store them 
alphabetically. To keep the task simple, let’s assume that all the values in 
the list are lowercase.'''

#cars = ["honda", "audi", "nissan", "toyota"]
#cars.sort()
#print(cars)

'''You can also sort this list in reverse alphabetical order by passing the 
argument reverse=True to the sort() method.'''

#cars.sort(reverse=True)
#print(cars)

### VERY IMPORTANT ###

'''Sorting a list alphabetically is a bit more complicated when all the values are not in 
lowercase. There are several ways to interpret capital letters when determining a sort 
order, and specifying the exact order can be more complex than we want to deal with 
at this time. However, most approaches to sorting will build directly on what you 
learned in this section.'''

### PRINTING A LIST IN REVERSE ORDER ### 

'''To reverse the original order of a list, you can use the reverse() method.'''

#cars = ["honda", "audi", "nissan", "toyota"]
#cars.reverse()
#print(cars)

### FINDING THE LENGTH OF A LIST ###

'''You can quickly find the length of a list by using the len() function.'''

cars = ["honda", "audi", "nissan", "toyota"]
len(cars)
print(len(cars))

'''You’ll find len() useful when you need to identify the number of aliens 
that still need to be shot down in a game, determine the amount of data 
you have to manage in a visualization, or figure out the number of registered 
users on a website, among other tasks.'''

