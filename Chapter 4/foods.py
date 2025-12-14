### Copying a List ###

''' Often, you’ll want to start with an existing list and make an entirely new list 
based on the first one. Let’s explore how copying a list works and examine 
one situation in which copying a list is useful.
To copy a list, you can make a slice that includes the entire original list 
by omitting the first index and the second index ([:]). This tells Python to 
make a slice that starts at the first item and ends with the last item, producing 
a copy of the entire list.'''

#my_foods = ["pizza", "falafel", "carrot cake"]
#friends_food = my_foods[:]

#print("My favourite foods are:")
#print(my_foods)

#print("\nMy friend´s favourite foods are:")
#print(friends_food)

'''To prove that we actually have two separate lists, we’ll add a new food 
to each list and show that each list keeps track of the appropriate person’s 
favorite foods:'''

my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]

my_foods.append('cannoli')
friends_foods.append('ice cream')

print(my_foods)
print(friends_foods)

''' The output shows that 'cannoli' now appears in our list of favorite 
foods but 'ice cream' doesn’t. We can see that 'ice cream' now appears 
in our friend’s list but 'cannoli' doesn’t. If we had simply set friend_foods 
equal to my_foods, we would not produce two separate lists.'''

# This doesn't work:
friend_foods = my_foods

''' Instead of storing a copy of my_foods in friend_foods at u, we set friend 
_foods equal to my_foods. This syntax actually tells Python to associate 
the new variable friend_foods with the list that is already associated with 
my_foods, so now both variables point to the same list. As a result, when we 
add 'cannoli' to my_foods, it will also appear in friend_foods. Likewise 'ice 
cream' will appear in both lists, even though it appears to be added only to 
friend_foods.'''

