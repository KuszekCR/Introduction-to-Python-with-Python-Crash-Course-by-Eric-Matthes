### NUMBERS ###

''' Numbers are used quite often in programming to keep score in games, 
represent data in visualizations, store information in web applications, 
and so on. Python treats numbers in several different ways, depending on 
how they’re being used. Let’s first look at how Python manages integers, 
because they’re the simplest to work with.'''

number1 = 5 + 7
number2 = 13 - 4
number3 = 2 * 7
number4 = 25 / 5 #Divisions always return float numbers
number5 = 2 ** 5

#print(number1)
#print(number2)
#print(number3)
#print(number4)
#print(number5)

number6 = 2 * (3 + 4)
#print(number6)

### FLOATS ###

''' Python calls any number with a decimal point a float. This term is used 
in most programming languages, and it refers to the fact that a decimal 
point can appear at any position in a number. '''

var_1 = 0.2
var_2 = 0.1
#print (var_1 + var_2)

''' The last print will will return 0.30000000000000004 as a result. This happens in all 
languages and is of little concern. Python tries to find a way to represent the result as 
precisely as possible, which is sometimes difficult given how computers have to represent numbers internally. '''


### UNDERSOCRES IN NUMBERS ### 
''' When you’re writing long numbers, you can group digits using underscores 
to make large numbers more readable: '''

universe_age = 14_000_000_000
# When you print a number that was defined using underscores, Python prints only the digits:
#print(universe_age)

### MULTIPLE ASSIGNMENT ### 
''' You can assign values to more than one variable using just a single line. 
This can help shorten your programs and make them easier to read; you’ll 
use this technique most often when initializing a set of numbers.
For example, here’s how you can initialize the variables x, y, and z 
to zero: '''

x, y, z = 0, 0, 0 

''' You need to separate the variable names with commas, and do the 
same with the values, and Python will assign each value to its respectively 
positioned variable. As long as the number of values matches the number of 
variables, Python will match them up correctly.'''

fav_number = 8

print("Hello, my name is Rodrigo and my favourite number is", fav_number)
 