''' In Chapter 3 you learned how to make a simple list, and you learned to work with 
the individual elements in a list. In this chapter you’ll learn how to loop through an entire 
list using just a few lines of code regardless of how long the list is. Looping allows 
you to take the same action, or set of actions, with every item in a list. As a result, 
you’ll be able to work efficiently with lists of any length, including those with thousands 
or even millions of items.'''


### LOOPING THROUGH AN ENTIRE LIST ### 

''' You’ll often want to run through all entries in a list, performing the same 
task with each item. For example, in a game you might want to move every 
element on the screen by the same amount, or in a list of numbers you 
might want to perform the same statistical operation on every element. Or 
perhaps you’ll want to display each headline from a list of articles on a web
site. When you want to do the same action with every item in a list, you can 
use Python’s for loop.
Let’s say we have a list of magicians’ names, and we want to print out 
each name in the list. We could do this by retrieving each name from the 
list individually, but this approach could cause several problems. For one, 
it would be repetitive to do this with a long list of names. Also, we’d have to 
change our code each time the list’s length changed. A for loop avoids both 
of these issues by letting Python manage these issues internally.'''

#magicians = ['alice', 'david', 'carolina'] 
#for magician in magicians: 
#    print(magician.title())

'''We begin by defining a list, just as we did in Chapter 3. Then
we define a for loop. This line tells Python to pull a name from the list 
magicians, and associate it with the variable magician. Then we tell Python to 
print the name that’s just been assigned to magician. Python then repeats 
the lines, once for each name in the list. It might help to read this 
code as “For every magician in the list of magicians, print the magician’s 
name.”'''

#magicians = ['alice', 'david', 'carolina'] 
#for magician in magicians: 
#    print(f"{magician.title()}, that was a great trick!")

''' You can also write as many lines of code as you like in the for loop. 
Every indented line following the line for magician in magicians is considered
inside the loop, and each indented line is executed once for each 
value in the list. Therefore, you can do as much work as you like with 
each value in the list.'''

#magicians = ['alice', 'david', 'carolina'] 
#for magician in magicians: 
#    print(f"{magician.title()}, that was a great trick!")
#    print(f"I cannot wait to see your next trick, {magician.title()}.\n")

''' Any lines of code after the for loop that are not indented are executed 
once without repetition.'''

#print("Thank you, everyone. That was a great magic show!")

### AVOIDING INDENTATION ERRORS ### 

''' Python uses indentation to determine how a line, or group of lines, is related 
to the rest of the program. In the previous examples, the lines that printed 
messages to individual magicians were part of the for loop because they 
were indented. Python’s use of indentation makes code very easy to read. 
Basically, it uses whitespace to force you to write neatly formatted code 
with a clear visual structure. In longer Python programs, you’ll notice 
blocks of code indented at a few different levels. These indentation levels 
help you gain a general sense of the overall program’s organization. 
As you begin to write code that relies on proper indentation, you’ll 
need to watch for a few common indentation errors. For example, people 
sometimes indent lines of code that don’t need to be indented or forget 
to indent lines that need to be indented.'''

### FORGETTING TO INDENT ADDITIONAL LINES ###

''' Sometimes your loop will run without any errors but won’t produce the 
expected result. This can happen when you’re trying to do several tasks in 
a loop and you forget to indent some of its lines.'''

#magicians = ['alice', 'david', 'carolina'] 
#for magician in magicians: 
#    print(f"{magician.title()}, that was a great trick!")
#print(f"I can't wait to see your next trick, {magician.title()}.\n")

''' The call to print() is supposed to be indented, but because Python 
finds at least one indented line after the for statement, it doesn’t report an 
error. As a result, the first print() call is executed once for each name in the 
list because it is indented. The second print() call is not indented, so it is 
executed only once after the loop has finished running. Because the final 
value associated with magician is 'carolina', she is the only one who receives 
the “looking forward to the next trick” message.'''

''' This is a logical error. The syntax is valid Python code, but the code does 
not produce the desired result because a problem occurs in its logic. If you 
expect to see a certain action repeated once for each item in a list and it’s 
executed only once, determine whether you need to simply indent a line or 
a group of lines.'''

### INDENTING UNNECESSARILY ###

''' If you accidentally indent a line that doesn’t need to be indented, Python 
informs you about the unexpected indent.'''

#msg = "Hello World"
    #print(msg) # We don’t need to indent the print() call, because it isn’t part of a loop!

### FORGETTING THE COLON ###

'''The colon at the end of a for statement tells Python to interpret the next 
line as the start of a loop.'''

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians
    print(magician) # It´ll return: SyntaxError: expected ':'

