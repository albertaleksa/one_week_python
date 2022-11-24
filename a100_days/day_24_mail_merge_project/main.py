#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
# letter_for_name.txt
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"


def read_starting_letter(name):
    with open(name) as file:
        letter = file.read()
    return letter


def read_names(name):
    with open(name) as file:
        names = file.readlines()
    return names


def save_letter(name, letter):
    letter_path = f"./Output/ReadyToSend/letter_for_{name}.txt"
    with open(letter_path, mode="w") as file:
        file.write(letter)


def create_emails():
    starting_letter = read_starting_letter("./Input/Letters/starting_letter.txt")
    names = read_names("./Input/Names/invited_names.txt")
    for name in names:
        name = name.strip()
        new_letter = starting_letter.replace(PLACEHOLDER, name)
        save_letter(name, new_letter)


if __name__ == "__main__":
    create_emails()
