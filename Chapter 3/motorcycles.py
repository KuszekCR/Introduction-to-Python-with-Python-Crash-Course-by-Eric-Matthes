### CHANGING, ADDING AND REMOVING ELEMENTS ###

''' Most lists you create will be dynamic, meaning you’ll build a list and 
then add and remove elements from it as your program runs its course. For 
example, you might create a game in which a player has to shoot aliens out 
of the sky. You could store the initial set of aliens in a list and then remove 
an alien from the list each time one is shot down. Each time a new alien 
appears on the screen, you add it to the list. Your list of aliens will increase 
and decrease in length throughout the course of the game.'''

### Modifying Elements in a List ###

#motorcycles = ["honda", "yamaha", "kawasaki", "motomel", "vespa"]
#print(motorcycles)

#motorcycles[0] = "ducati" # It replaced the element of the previous list, in the 1st position of it.
#print(motorcycles) 

### Adding Elements to a List ###

''' The simplest way to add a new element to a list is to append the item to the 
list. When you append an item to a list, the new element is added to the end 
of the list.'''

#motorcycles.append("ducati")
#print(motorcycles)

''' The append() method makes it easy to build lists dynamically. For 
example, you can start with an empty list and then add items to the list 
using a series of append() calls.'''

#motorcycles = []

#motorcycles.append("Honda")
#print(motorcycles)
#motorcycles.append("Motomel")
#print(motorcycles)
#motorcycles.append("Ducati")
#print(motorcycles)
#motorcycles.append("Vespa")
#print(motorcycles)

### Removing Elements from a List ###

''' Often, you’ll want to remove an item or a set of items from a list. For 
example, when a player shoots down an alien from the sky, you’ll most 
likely want to remove it from the list of active aliens. Or when a user 
decides to cancel their account on a web application you created, you’ll 
want to remove that user from the list of active users. You can remove an 
item according to its position in the list or according to its value.'''

#motorcycles = ["honda", "yamaha", "kawasaki", "motomel", "vespa"]
#del motorcycles[0]
#print(motorcycles)

'''You can remove an item from any position in a list using the del state
ment if you know its index.'''

#del motorcycles[2]
#print(motorcycles)

'''In both examples, you can no longer access the value that was removed 
from the list after the del statement is used.'''

### Removing an Item Using the pop() Method ###

'''Sometimes you’ll want to use the value of an item after you remove it from a 
list. For example, you might want to get the x and y position of an alien that 
was just shot down, so you can draw an explosion at that position. In a web 
application, you might want to remove a user from a list of active members 
and then add that user to a list of inactive members.
 The pop() method removes the last item in a list, but it lets you work 
with that item after removing it. The term pop comes from thinking of a 
list as a stack of items and popping one item off the top of the stack. In 
this analogy, the top of a stack corresponds to the end of a list.'''

#motorcycles = ["honda", "yamaha", "kawasaki", "motomel", "vespa"]
#print(motorcycles)

#popped_motorcycles = motorcycles.pop() # It "picks up" the last element of the list. Its a single element from a list. 
#print(motorcycles) # The current list lacks the last element that was taken off by the pop() function.
#print(popped_motorcycles) # It returns the element popped off, which is always the LAST element of the list.

'''How might this pop() method be useful? Imagine that the motorcycles 
in the list are stored in chronological order according to when we owned 
them. If this is the case, we can use the pop() method to print a statement 
about the last motorcycle we bought.'''

#motorcycles = ["honda", "yamaha", "kawasaki", "motomel", "vespa"]
#last_owned = motorcycles.pop()
#print(f"The last motorcycle I bought is a {last_owned.title()}")

'''You can use pop() to remove an item from any position in a list by including 
the index of the item you want to remove in parentheses.'''

#first_owned = motorcycles.pop(0)
#print(f"The first bike that I owned is a {first_owned.title()}")

''' If you’re unsure whether to use the del statement or the pop() method, 
here’s a simple way to decide: when you want to delete an item from a list 
and not use that item in any way, use the del statement; if you want to use an 
item as you remove it, use the pop() method.'''

### Removing an Item by Value ###

''' Sometimes you won’t know the position of the value you want to remove 
from a list. If you only know the value of the item you want to remove, you 
can use the remove() method.'''

motorcycles = ["honda", "yamaha", "kawasaki", "motomel", "vespa"]
#print(motorcycles)

#motorcycles.remove("kawasaki") # Kawasaki has been deleted from the list.
#print(motorcycles)

'''You can also use the remove() method to work with a value that’s being 
removed from a list.'''

print(motorcycles)
too_expensive = "kawasaki"
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\n A {too_expensive.title()} is too expensive for me.") # \n is utilized to leave a blank line.


