
print("Welcome to the game!")
player_1 = input("enter player 1's name: ")
player_2 = input("enter player 2's name: ")
current_player = player_1

toothpick_count = 13

while True:
    print("|  " * toothpick_count)
    print(f"There are {toothpick_count} toothpicks left")
    pl1_count = int(input(f"How many do you take, {current_player} ? "))
    while pl1_count not in [1, 2, 3]:
        pl1_count = int(input(f"You can only take 1, 2, or 3: "))
    toothpick_count -= pl1_count
    if toothpick_count <= 0:
        print(f"{current_player} wins!!!")
        break
    if current_player == player_1:
        current_player = player_2
    else:
        current_player = player_1


print("GAME OVER!!")




