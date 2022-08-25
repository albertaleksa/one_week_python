import random

dices_count = int(input("How many dice are we rolling? "))
sides_count = int(input("How many sides on each die? "))

while dices_count not in range(1, 21) or sides_count not in range(1, 21):
    print("Please enter a valid integer between 1 and 20")
    dices_count = int(input("How many dice are we rolling? "))
    sides_count = int(input("How many sides on each die? "))

while True:
    for dices in range(dices_count):
        print(f"|{random.randint(1, sides_count)}", end="")
    print("|")
    quit = input("Roll again? ('q' to quit) ")
    if quit == 'q':
        break
