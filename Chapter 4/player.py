### WORKING WITH PART OF A LIST ### 


### Slicing a List ###

'''To make a slice, you specify the index of the first and last elements you 
want to work with. As with the range() function, Python stops one item 
before the second index you specify. To output the first three elements 
in a list, you would request indices 0 through 3, which would return elements 0, 1, and 2.'''


players = ["carlos", "martina", "joaquin", "ana", "florencia"]
#print(players[0:3]) 

'''The code prints a slice of this list, which includes just the first 
three players. The output retains the structure of the list and includes the 
first three players in the list'''

# You can generate any subset of a list:

#print(players[1:4]) #It won´t include the last element, always stops at the previous one.

# Without a starting index, Python starts at the beginning of the list:

print(players[:4])

# A similar syntax works if you want a slice that includes the end of a list:

#print(players[2:])

'''Recall that a negative index returns an element a certain distance from the end of a list; 
therefore, you can output any slice from the end of a list.'''

#print(players[-4:])

'''This prints the names of the last three players and would continue to 
work as the list of players changes in size.'''

### Looping Through a Slice ###

'''You can use a slice in a for loop if you want to loop through a subset of 
the elements in a list. In the next example we loop through the first three 
players and print their names as part of a simple roster:'''

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

'''Slices are very useful in a number of situations. For instance, when you’re 
creating a game, you could add a player’s final score to a list every time that 
player finishes playing. You could then get a player’s top three scores by sort
ing the list in decreasing order and taking a slice that includes just the first 
three scores. When you’re working with data, you can use slices to process 
your data in chunks of a specific size. Or, when you’re building a web application, 
you could use slices to display information in a series of pages with 
an appropriate amount of information on each page.'''

