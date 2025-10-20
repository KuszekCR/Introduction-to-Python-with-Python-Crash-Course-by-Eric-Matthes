'''3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who 
would you invite? Make a list that includes at least three people you’d like to 
invite to dinner. Then use your list to print a message to each person, inviting 
them to dinner.'''

#list_of_people = ["di stefano", "alan turing", "'locomotora' oliveras", "ariel ortega"]
#last_invited = list_of_people.pop()
#print(f"Good morning {last_invited.title()}, you have been invited to a fancy dinner with me!")
#last_invited = list_of_people.pop()
#print(f"Good morning {last_invited.title()}, you have been invited to a fancy dinner with me!")
#last_invited = list_of_people.pop()
#print(f"Good morning {last_invited.title()}, you have been invited to a fancy dinner with me!")
#last_invited = list_of_people.pop()
#print(f"Good morning {last_invited.title()}, you have been invited to a fancy dinner with me!")

'''3-5. Changing Guest List: You just heard that one of your guests can’t make the 
dinner, so you need to send out a new set of invitations. You’ll have to think of 
someone else to invite.
 •	Start with your program from Exercise 3-4. Add a print() call at the end 
of your program stating the name of the guest who can’t make it.
 •	Modify your list, replacing the name of the guest who can’t make it with 
the name of the new person you are inviting.
 •	Print a second set of invitation messages, one for each person who is still 
in your list.'''

#list_of_people = ["di stefano", "alan turing", "'locomotora' oliveras", "ariel ortega"]
#unavailable = "ariel ortega" 
#list_of_people.remove(unavailable)
#print(list_of_people)
#print(f"\n {unavailable.title()} is unable to assist to the dinner.")

#list_of_people.append("marcelo gallardo")
#print(list_of_people)

#last_invited = list_of_people.pop()
#print(f"Good morning {last_invited.title()}, you are still invited to a fancy dinner with me!")
#last_invited = list_of_people.pop()
#print(f"Good morning {last_invited.title()}, you are still invited to a fancy dinner with me!")
#last_invited = list_of_people.pop()
#print(f"Good morning {last_invited.title()}, you are still invited to a fancy dinner with me!")
#last_invited = list_of_people.pop()
#print(f"Good morning {last_invited.title()}, you are still invited to a fancy dinner with me!")

''' 3-6. More Guests: You just found a bigger dinner table, so now more space is 
available. Think of three more guests to invite to dinner.
 •	Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() 
call to the end of your program informing people that you found a bigger 
dinner table.
 •	Use insert() to add one new guest to the beginning of your list.
 •	Use insert() to add one new guest to the middle of your list.
 •	Use append() to add one new guest to the end of your list.
 •	Print a new set of invitation messages, one for each person in your list.'''

#list_of_people = ["di stefano", "alan turing", "'locomotora' oliveras", "ariel ortega"]
#del list_of_people[3]
#list_of_people.insert(0, "leo messi")
#list_of_people.insert(3, "dot dager")
#list_of_people.append("felix kjellberg")

#print(list_of_people)

'''3-7. Shrinking Guest List: You just found out that your new dinner table won’t 
arrive in time for the dinner, and you have space for only two guests.
 •	Start with your program from Exercise 3-6. Add a new line that prints a 
message saying that you can invite only two people for dinner.
 •	Use pop() to remove guests from your list one at a time until only two 
names remain in your list. Each time you pop a name from your list, print 
a message to that person letting them know you’re sorry you can’t invite 
them to dinner.
 •	Print a message to each of the two people still on your list, letting them 
know they’re still invited.
 •	Use del to remove the last two names from your list, so you have an empty 
list. Print your list to make sure you actually have an empty list at the end 
of your program.'''

new_list = ['leo messi', 'di stefano', 'alan turing', 'dot dager', "'locomotora' oliveras", 'felix kjellberg']

last_invited = new_list.pop()
print(f"We are deepply sorry {last_invited.title()}, unfortunately we only have 2 spaces for dinner, therefore we cannot continue with the invite. We are deeply sorry about that!")
last_invited = new_list.pop()
print(f"We are deepply sorry {last_invited.title()}, unfortunately we only have 2 spaces for dinner, therefore we cannot continue with the invite. We are deeply sorry about that!")
last_invited = new_list.pop()
print(f"We are deepply sorry {last_invited.title()}, unfortunately we only have 2 spaces for dinner, therefore we cannot continue with the invite. We are deeply sorry about that!")
last_invited = new_list.pop()
print(f"We are deepply sorry {last_invited.title()}, unfortunately we only have 2 spaces for dinner, therefore we cannot continue with the invite. We are deeply sorry about that!")

print(new_list)

guest_1 = "di stefano"
new_list.remove(guest_1)
print(new_list)
print(f"\nA {guest_1.title()}, you are still invited to dinner with me!")

guest_2 = "leo messi"
new_list.remove(guest_2)
print(f"\nA {guest_2.title()}, you are still invited to dinner with me!")

print(new_list)
