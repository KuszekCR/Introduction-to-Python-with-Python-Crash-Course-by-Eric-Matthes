''' 3-8. Seeing the World: Think of at least five places in the world you’d like to 
visit. 
 •	Store the locations in a list. Make sure the list is not in alphabetical order.
 •	Print your list in its original order. Don’t worry about printing the list neatly, 
just print it as a raw Python list.
 •	Use sorted() to print your list in alphabetical order without modifying the 
actual list.
 •	Show that your list is still in its original order by printing it.
 •	Use sorted() to print your list in reverse alphabetical order without chang
ing the order of the original list.
 •	Show that your list is still in its original order by printing it again.
 •	Use reverse() to change the order of your list. Print the list to show that its 
order has changed.
 •	Use reverse() to change the order of your list again. Print the list to show 
it’s back to its original order.
 •	Use sort() to change your list so it’s stored in alphabetical order. Print the 
list to show that its order has been changed.
 •	Use sort() to change your list so it’s stored in reverse alphabetical order. 
Print the list to show that its order has changed.'''

places_to_visit = ["tokio", "galápagos", "nueva york", "málaga", "marruecos", "egipto"]

#print(places_to_visit)

#print(sorted(places_to_visit)) # It temporarily sorts the previous list alphabetically.

#print(places_to_visit) # Here we see that the list still contains the elements sorted the original way.

#print(sorted(places_to_visit, reverse=True)) # I got it right 1st try :D

#print(places_to_visit)

#places_to_visit.reverse()
#print(places_to_visit) 

#places_to_visit.reverse()
#print(places_to_visit) # We just reversed the previously reversed list. We got the original list back!

#places_to_visit.sort()
#print(places_to_visit)

#places_to_visit.sort(reverse=True)
#print(places_to_visit)


''' 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 
through 3-7 (page 42), use len() to print a message indicating the number 
of people you are inviting to dinner.'''

#list_of_people = ["di stefano", "alan turing", "'locomotora' oliveras", "ariel ortega"]
#print("We have invitations for", len(list_of_people), "people.")

'''3-10. Every Function: Think of something you could store in a list. For example, 
you could make a list of mountains, rivers, countries, cities, languages, or any
thing else you’d like. Write a program that creates a list containing these items 
and then uses each function introduced in this chapter at least once.'''

sudamerica = ["argentina", "brazil", "chile", "uruguay", "venezuela", "ecuador", "colombia", "paraguay", "bolivia", "peru"]
print(sudamerica)
print(sorted(sudamerica))
print(sudamerica) #The list mantains its original form.

print(sorted(sudamerica, reverse=True))
print(sudamerica)

sudamerica.insert(10, "surinam")
print(sudamerica)

sudamerica.append("guyana")
print(sudamerica)

del sudamerica[11]
print(sudamerica)
del sudamerica[10]
print(sudamerica)

popped_peru = sudamerica.pop()
print(sudamerica)
print(popped_peru)

popped_argentina = sudamerica.pop(0)
print(sudamerica)
print(popped_argentina)

sudamerica.remove("brazil")
print(sudamerica)