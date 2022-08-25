import random

first_dice = random.randint(1, 6)
second_dice = random.randint(1, 6)
count = 0

while first_dice != 1 or second_dice != 1:
    print(f"{first_dice} - {second_dice}")
    first_dice = random.randint(1, 6)
    second_dice = random.randint(1, 6)
    count += 1

print(f"{first_dice} - {second_dice}")
print("SNAKE EYES!!!")
print(f"{count} counts")
