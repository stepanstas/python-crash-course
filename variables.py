# Store a message in a variable and then print that variable 

message = "Hello World! This is a message!"
print(message)

# Store a message in a variable, and print that message. Then change the value of your variable to a new message, and print that new message 
message = "This is a new message!"
print(message)

# Store a person's name in a variable, and print a message to that person. Your message should be simple, such as, "Hello Bison, would you like to learn some Python today?"
name = "Bison"
message = "Hello " + name + ", would you like to learn some Python today?"
print(message)

# Store a person's name in a variable, and then print that person's name in lowercase, uppercase, and titlecase 
person_name = "Bison"
print(person_name.lower())
print(person_name.upper())
print(person_name.title())


# Find a famous quote from a person that you admire. Print the quote and the name of its author.
first_name = "Aajonus"
last_name = "Vonderplanitz"
quote = first_name + " " + last_name + " once said, 'Anything the medical profession says, do the opposite 99 percent of the time and you\'ll be right.'"
print(quote)

# Stripping whitespace. Store a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination. "\t" and "\n" at least once. 

person_name = "Names:\n\tBison\n\tBison\n\tBison\n"
print(person_name)

# Print person's name once so that whitespace around the name is displayed. Then print the name using each of the htree stripping functions, lstrip(), rstrip(), and strip()

person_name = " Bison     "
print(person_name.rstrip())
print(person_name.lstrip())
print(person_name.strip())

# Add, subtract, multiply and divide 

print(2 + 3)
print(3 - 2)
print(2 * 3)
print(3 / 2)

# Exponents 

exponent = 3 ** 2
print(exponent)
print(5 ** 5)

# Store your favorite number in a variable. Then using that variable, create a message that reveals your favorite number. Print that message. 

favorite_number = 12
message = "My favorite number is " + str(favorite_number) # the variable is wrapped in the string function which tells Python to represent non-string values as strings 
print(message)

# This is a comment

