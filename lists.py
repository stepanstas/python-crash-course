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

# Make a list of three people, dead or alive, you'd like to invite to dinner. Then use the list to print a message to each person, inviting them to dinner. 

people = ["Aajonus Vonderplanitz", "Ray Peat", "Elon Musk"]
for person in people:
    message = ", I am inviting you to have dinner with me."
    print(person + message)
    
# You just heard that some of your guests cannot make it. 
declined = people.pop()
print(declined + " is busy and unable to make it.")
deceased = people[0]
dead = people[1]
print(deceased + " and " + dead + " are both dead so they can't make it either.")

# Modify the list replacing the names of the guests who can't make it with the new people you are inviting.

people = []
people.append("Mommy")
people.append("Daddy")
people.append("Grandma")
print(people)
for person in people:
    message = ", I am inviting you to have dinner with me."
    print(person + message)
# Add a print statement informing people that you found a bigger table
print ("I found a bigger table.")

# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

# Use insert to add one new guest to the beginning of your list 
people.insert(0, "Grandpa")

# Use insert to add one new guest to the middle of your list
people.insert(2, "Auntie")

# Use append to add one new guest to the end of your lost
people.append("Cousin")

for person in people:
    print(person + message)




