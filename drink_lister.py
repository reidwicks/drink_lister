#!usr/bin/python

"""
cocktail_lister

Allows user to create a cocktail (or really anything), and list its 
ingredients. Ingredients are organised into sets so the user can see what
ingredients they need to buy, and what ingredients they have to work with,
if they're trying to use a limited number of ingredients across many drinks.

Obviously designed more with functionality in mind that user-friendliness. Will
look at adding a UI in the future.
"""

drinks = {}
cupboard = []

class Drink():
    def __init__(self, name):
        self.name = name
        self.ingredients = []
            
def menu():
    print(  
"""1. Add drink
2. Modify drink
3. List drinks and ingredients
4. Enter what you already own
5. Create grocery list
6. Save to file
7. Quit"""
        )
    while True:                
        answer = input()
        if answer.isdigit() == False:
            print("That is not an option.")
        elif int(answer) == 1:
            add_drink()
            break
        elif int(answer) == 2:
            modify_drink()
            break
        elif int(answer) == 3:
            list_drinks()
            input()
            break
        elif int(answer) == 4:
            already_own()
            break
        elif int(answer) == 5:
            grocery_list()
            break
        elif int(answer) == 6:
            save_to_file()
            break
        elif int(answer) == 7:
            quit()
        else:
            print("That is not an option")
        
def add_drink():
    print("What drink would you like to add?")
    name = input()
    new_drink = Drink(name)
    print("What ingredients are in the", new_drink.name + "?"
        , "\n(when you're finished adding ingredients, type \"done\")")
    while True:
        addition = input()
        if addition == "done":
            break
        new_drink.ingredients.append(addition)
    drinks.update({name : new_drink})
    
def modify_drink():
    print("What drink would you like to modify?")
    print("So far you have:")
    list_drinks()
    selected_drink = None
    while selected_drink == None:
        selection = input()
        for item in drinks:
            if item.lower() == selection.lower():
                selected_drink = drinks[item]
                break
            else:
                print("Please select a valid drink")
        break
    print("Would you like to..?")
    print("1. Add ingredients", "\n2. Remove ingredients", "\n3. Rename drink")
    while True:
        answer = input()
        if answer.isdigit == False:
            print("That is not an option.")
        elif int(answer) == 1:
            add_ingred(selected_drink)
            break
        elif int(answer) == 2:
            remove_ingred(selected_drink)
            break
        elif int(answer) == 3:
            rename_drink(selected_drink)
            break
        else:
            print("That is not an option.")

def add_ingred(selected_drink):
    print(  "What ingredients would you like to add to the", selected_drink.name + "?", 
            "\n(when finished adding ingredients, type \"done\")")
    while True:
        addition = input()
        if addition == "done":
            break
        selected_drink.ingredients.append(addition)
    
def remove_ingred(selected_drink):
    print(  "What ingredients would you like to remove from the", selected_drink.name + "?", 
            "\n(when finished removing ingredients, type \"done\")")
    print("You currently have:")
    for ingredient in selected_drink.ingredients:
        print("  " + ingredient)
    while True:
        removal = input()
        if removal == "done":
            break
        for ingredient in selected_drink.ingredients:
            if removal.lower() == ingredient:
                selected_drink.ingredients.remove(ingredient)
    
def rename_drink(selected_drink):
    print("Renaming " + selected_drink.name + ".")
    new_name = input("New name: ")
    new_drink = Drink(new_name)
    new_drink.ingredients = selected_drink.ingredients
    drinks.update({new_name : new_drink})
    del drinks[selected_drink.name]
    
def list_drinks():
    if not drinks:
        print("You haven't added any drinks yet.")
    else:
        for item in drinks:
            print(item + ":")
            for ingr in drinks[item].ingredients:
                print("  " + ingr)
            if not drinks[item].ingredients:
                print("  No ingredients added.")
        
def save_to_file():
    filename = input("Please type a filename. \n")
    f = open(filename + ".txt", "w")
    f.write("Drinks:\n\n")
    for item in drinks:
        f.write(item + ":\n")
        for ingr in drinks[item].ingredients:
            f.write("  " + ingr + "\n")
        if not drinks[item].ingredients:
            f.write("  No ingredients added.\n")
        f.write("\n")
    all_ingredients = []
    for item in drinks:
        for ingredient in drinks[item].ingredients:  
            all_ingredients.append(ingredient)
    all_ingredients = set(all_ingredients)
    cupboard_set = set(cupboard)
    shopping_list = all_ingredients.difference(cupboard_set)
    f.write("Things you have:\n")
    for item in cupboard:
        f.write("  " + item + "\n")
    f.write("\nGrocery list:\n")
    for item in shopping_list:
        f.write("  " + item + "\n")
    f.close()
    print("File created")
    
def already_own():
    print("What ingredients do you have in your cupboard?",
            "\n(when you're done, type \"done\")")
    while True:
        addition = input()
        if addition == "done":
            break
        cupboard.append(addition)

def grocery_list():
    all_ingredients = []
    for item in drinks:
        for ingredient in drinks[item].ingredients:  
            all_ingredients.append(ingredient)
    print("Things you have:")
    for item in cupboard:
        print("  " + item)
    print("Shopping list:")
    all_ingredients = set(all_ingredients)
    cupboard_set = set(cupboard)
    shopping_list = all_ingredients.difference(cupboard_set)
    for item in shopping_list:
        print("  " + item)

while True:
    menu()
