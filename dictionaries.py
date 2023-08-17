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