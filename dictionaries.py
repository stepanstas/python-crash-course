"""
Use a dictionary to store information about a person you know. Store their name, age, the city and state in which they live. You should have keys such as name, age, city.and state. Print each piece of information stored in your dictionary.

"""

person = {
    "name": "Bison",
    "age": "4",
    "city": "west yellowstone",
    "state": "wyoming",
}

for key, value in person.items():
    print(f"{key}: {value}")
    
"""
Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

"""

favorite_numbers = {
    "Jan": 35,
    "Milan": 22,
    "Jana": 10,
    "Milana": 39,
}

for name, number in favorite_numbers.items():
    print(f"{name}: {number}")
    
"""
A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character ('\n') to insert a blank line between each word-meaning pair in your output.

"""

glossary = {
    "string": "A series of characters.",
    "comment": "A note in a program that the Python interpreter ignores.",
    "list": "A collection of items in a particular order.",
    "loop": "Work through a collection of items, one at a time.",
    "dictionary": "A collection of key-value pairs.",
}

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
    