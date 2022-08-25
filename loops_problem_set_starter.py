
#  ----------
#    PART 1
#  ----------
word = "supercalifragilisticexpialidocious"

# Write a for loop that prints out each character in the above "word" variable
for ch in word:
    print(ch)

# Write a while loop that does the same thing!
index = 0
while index < len(word):
    print(word[index])
    index += 1

#  ----------
#    PART 2
#  ----------
# Write a while loop that prints the even numbers from 100 to 140 (including 140)
number = 100
while number <= 140:
    print(number)
    number += 2




# Write a for loop that does the same thing (with range())
for num in range(100, 141, 2):
    print(num)

#  ----------
#    PART 3
#  ----------
# Write a loop that asks a user to input the passphrase "sillygoose" and keeps asking them to do so until they comply:
passphrase = ""
while passphrase != "sillygoose":
    passphrase = input('Please input the passphrase "sillygoose": ')

