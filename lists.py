# Store names in a list called names 
names = ["Bison", "Bear", "Fox", "Puma"]

# Print each person's name by accessing each element in the list one at a time 
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# Print a message to the names with the same text but personalized with the name.
for name in names:
    message = "I am a " + name.lower() + " and I am an animal!"
    print(message)
    
    
# Think of your favorite animals and make a list that stores several examples. Use the list to print a series of statements about these animals. 

animals = ["Grizzly Bear", "Mountain Lion", "Moose"]

statement = " is a wild animal!"

for animal in animals:
    print(animal + statement)

griz_fact = " will maul you to death!"
lion_fact = " will bite your neck!"
moose_fact = " will trample you!"

print(animals[0] + griz_fact)
print(animals[1] + lion_fact)
print(animals[2] + moose_fact)

