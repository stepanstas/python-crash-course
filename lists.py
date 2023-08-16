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
    
# Use pop to remove guests from your list until only two names remain in your list. 
removed_guest = people.pop()
print("I am sorry" + removed_guest + " but I cannot invite you to dinner today.")
removed_guest = people.pop()
print("I am sorry" + removed_guest + " but I cannot invite you to dinner today.")
removed_guest = people.pop()
print("I am sorry" + removed_guest + " but I cannot invite you to dinner today.")
removed_guest = people.pop()
print("I am sorry" + removed_guest + " but I cannot invite you to dinner today.")

print(people)

for person in people: 
    print(person + "," + " you're still invited to dinner!")
    
# Empty out the list    
del people[1]
print(people)
del people[0]
print(people)

''' Think of at least five places in the world you’d like to visit.

Store the locations in a list. Make sure the list is not in alphabetical order.
Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
Use sorted() to print your list in alphabetical order without modifying the actual list.
Show that your list is still in its original order by printing it.
Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
Show that your list is still in its original order by printing it again.
Use reverse() to change the order of your list. Print the list to show that its order has changed.
Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed. 

'''

locations = ['switzerland', 'colombia', 'canada', 'italy', 'spain']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

# Use length to indicate the number of places you'd like to visit
print(len(locations))

'''
Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.

Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!

'''

pizzas = ['mushroom', 'garlic', 'cheese']

for pizza in pizzas:
    print(pizza.title())
    print("In lowercase: " + pizza.lower())
    print("In uppercase: " + pizza.upper())
    
for pizza in pizzas:
    print(f"I like {pizza} pizza!")
print("\nCan't you tell that I really love pizza?!")

'''
Think of at least three kinds of your favorite animals. Store these animals names in a list, and then use a for loop to print the name of each animal.

Modify your for loop to print a sentence using the name of the animal instead of printing just the name of the animal. For each animal you should have one line of output containing a simple statement.
Add a line at the end of your program with a statement about the animals.

'''

animals = ['bear', 'mountain lion', 'mooose']

for animal in animals:
    print(animal.title())
    
for animal in animals:
    print(f"{animal.title()} can be a dangerous wild animal!")
print("\nAll of these animals are fascinating if you're lucky to ever encounter them in the wild")

# Use a for loop to print the numbers from 1 to 20, inclusive.
for number in range(1,21):
    print(number)
    
# Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

numbers = list(range(1, 1000001))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# Odd numbers. Make a list of odd numbers from 1 to 20. Use a for loop to print each odd number.
numbers = list(range(1,21,2))
for number in numbers:
    print(number)

# Threes. Make a list of multiples from 3 to 30. Use a for loop to print the numbers in your list. 
numbers = list(range(3,31,3))
for number in numbers:
    print(number)
    
# Make a list of first ten cubes and use a for loop to print out the value of each cube.
cubes = []
for number in range(1,11):
    cube = number**3
    cubes.append(cube)
print(cubes)

# Use a list comprehension to generate a list of the first 10 cubes.
cubes = [number**3 for number in range(1,11)]
print(cubes)

