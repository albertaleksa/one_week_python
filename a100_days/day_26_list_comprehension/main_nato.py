import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(alphabet)


def generate_phonetic():
    input_word = input("Please, input your word: ")
    try:
        code_words = [alphabet[letter.upper()] for letter in input_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(code_words)


generate_phonetic()
