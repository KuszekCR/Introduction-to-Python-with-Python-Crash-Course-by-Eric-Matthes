''' 3-1. Names: Store the names of a few of your friends in a list called names. Print 
each person’s name by accessing each element in the list, one at a time. ''' 


names = ["gustavo", "joaquin", "lucia", "felipe", "facundo", "agustin"]
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
print(names[5].title())

''' 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just 
printing each person’s name, print a message to them. The text of each message should be
the same, but each message should be personalized with the person’s name. '''

message = f"Hola {names[0]}, cómo estás? No sabía que hoy vendrías."

#print("Hola", names[0].title(), ", cómo estás? No sabía que hoy vendrías.")
#print("Hola", names[1].upper(), ", cómo estás? No sabía que hoy vendrías.")
#print("Hola", names[2].title(), ", cómo estás? No sabía que hoy vendrías.")
#print("Hola", names[3].lower(), ", cómo estás? No sabía que hoy vendrías.")
#print("Hola", names[4].title(), ", cómo estás? No sabía que hoy vendrías.")
#print("Hola", names[5].capitalize(), ", cómo estás? No sabía que hoy vendrías.")
#print(message) # By changing the index number I can access to any element of the list. 

''' 3-3. Your Own List: Think of your favorite mode of transportation, such as a 
motorcycle or a car, and make a list that stores several examples. Use your list 
to print a series of statements about these items, such as “I would like to own a 
Honda motorcycle.” '''

cars = ['audi', 'bmw', 'toyota', 'honda', 'bugatti', 'nissan']

message_2 = f"""I would love to have a reliable car such as a {cars[2].capitalize()}, but since I was
a little kid I always wanted a {cars[4].capitalize()} because it seemed so fast and cool. I also loved 
the {cars[-1].capitalize()} series because of the models it had."""

print(message_2)

### TIP FOR LONG MESSAGES ###
#Correct: Using triple quotes
long_message = f"""This is a very long string 
                   that spans multiple lines."""  # noqa: F541
