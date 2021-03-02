def mad_libs():
    name = input("Please enter a name: ")
    food = input("Choose a food: ")
    place = input("Pick a place: ")
    drink = input("Name a drink: ")
    sentence1 = "There once was a person named " + name + "."
    sentence2 = "They loved to eat " + food + "."
    sentence3 = "After work they always went to " + place + ","
    sentence4 = "and would drink a tall glass of " + drink + " before bed."
    print(sentence1,sentence2,sentence3,sentence4)