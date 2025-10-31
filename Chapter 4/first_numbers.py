### NUMERICAL LISTS ###

'''Many reasons exist to store a set of numbers. For example, you’ll need to 
keep track of the positions of each character in a game, and you might want 
to keep track of a player’s high scores as well. In data visualizations, you’ll 
almost always work with sets of numbers, such as temperatures, distances, 
population sizes, or latitude and longitude values, among other types of 
numerical sets.
Lists are ideal for storing sets of numbers, and Python provides a 
variety of tools to help you work efficiently with lists of numbers. Once you 
understand how to use these tools effectively, your code will work well even 
when your lists contain millions of items.'''

### RANGE FUNCTION ###

''' Python’s range() function makes it easy to generate a series of numbers. '''

#for value in range(1, 5):
#    print(value)

'''In this example, range() prints only the numbers 1 through 4. This is 
another result of the off-by-one behavior you’ll see often in programming 
languages. The range() function causes Python to start counting at the first 
value you give it, and it stops when it reaches the second value you provide. 
Because it stops at that second value, the output never contains the end 
value, which would have been 5 in this case.''' 

# To print the numbers from 1 to 5, you would use range(1, 6):
#for value in range(1, 6):
#    print(value)

#for value in range(10):
#    print(value) #It´ll print from 0 to the argument -1.

### Using range() to Make a List of Numbers ###

'''If you want to make a list of numbers, you can convert the results of range() 
directly into a list using the list() function. When you wrap list() around a 
call to the range() function, the output will be a list of numbers.'''

#numbers = list(range(1, 6))
#print(numbers)

''' We can also use the range() function to tell Python to skip numbers in a 
given range. If you pass a third argument to range(), Python uses that value 
as a step size when generating numbers.'''

#even_numbers = list(range(2, 11, 2))
#print(even_numbers)

#odd_numbers = list(range(1, 10, 2))
#print(odd_numbers)

''' You can create almost any set of numbers you want to using the range() 
function. For example, consider how you might make a list of the first 10 
square numbers (that is, the square of each integer from 1 through 10). In 
Python, two asterisks (**) represent exponents. '''

#squares = []
#for value in range(1, 11):
#    square = value ** 2
#    squares.append(square)
#print(squares)

''' To write this code more concisely, omit the temporary variable square 
and append each new value directly to the list:'''

#squares = []
#for value in range(1,11):
#    squares.append(value**2)
#print(squares) 

### Simple Statistics with a List of Numbers ###

''' A few Python functions are helpful when working with lists of numbers. For 
example, you can easily find the minimum, maximum, and sum of a list of 
numbers.'''

#digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#print(min(digits))
#print(max(digits))
#print(sum(digits))

### List Comprehensions ###

''' The approach described earlier for generating the list squares consisted of 
using three or four lines of code. A list comprehension allows you to generate 
this same list in just one line of code. A list comprehension combines the 
for loop and the creation of new elements into one line, and automatically 
appends each new element. List comprehensions are not always presented 
to beginners, but I have included them here because you’ll most likely see 
them as soon as you start looking at other people’s code.'''

squares = [value**2 for value in range(1, 11)]
print(squares)

