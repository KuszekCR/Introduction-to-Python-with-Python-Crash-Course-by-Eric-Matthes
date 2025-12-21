'''4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five 
simple foods, and store them in a tuple.
•	Use a for loop to print each food the restaurant offers.
•	Try to modify one of the items, and make sure that Python rejects the 
change.
•	The restaurant changes its menu, replacing two of the items with different 
foods. Add a line that rewrites the tuple, and then use a for loop to print 
each of the items on the revised menu.'''

#buffet = ("Hamburger", "French Fries", "Pizza", "Salad", "Spaghetti")
#print(buffet)
#print(buffet[0])
#print(buffet[2])
#print(buffet[4])

#for foods in buffet:
#    print(foods)

#buffet[0] = "Ice Cream"
#buffet[2] = "Milkshake"

#print(buffet)

'''Error -> TypeError: 'tuple' object does not support item assignment'''

buffet = ("Hamburger", "French Fries", "Pizza", "Salad", "Spaghetti")
print("Old menu:")
for foods in buffet:
    print(foods)

buffet = ("Ice Cream", "French Fries", "Milkshake", "Salad", "Spaghetti")
print("\nNew Menu: ")
for foods in buffet:
    print(foods)