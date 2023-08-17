"""

A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

Use a for loop to print each food the restaurant offers.
Try to modify one of the items, and make sure that Python rejects the change.
The restaurant changes its menu, replacing two of the items with different foods. Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

"""

buffet_menu = ("noodles", "rice", "shrimp", "crab", "fried plantains")

for food in buffet_menu:
    print(food)
    
# buffet_menu[0] = "baked potatoes"
# print(buffet_menu)

buffet_menu = ("baked potatoes", "fried rice", "shrimp", "crab", "fried plantains")

print("We have updated our menu. You can now choose from:")
for food in buffet_menu: 
    print(food.title())