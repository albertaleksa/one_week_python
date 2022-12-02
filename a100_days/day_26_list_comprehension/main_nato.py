import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:
alphabet = {row.letter: row.code for (index, row) in data.iterrows()}
print(alphabet)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Please, input your word: ")
code_words = [alphabet[letter.upper()] for letter in input_word]

print(code_words)
