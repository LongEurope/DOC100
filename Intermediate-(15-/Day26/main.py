import pandas as pd

data = pd.read_csv(r'DOC100\Intermediate-(15-\Day26\nato_phonetic_alphabet.csv')

alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}

word = input('Enter a word: ').upper()

phon_word = [alpha_dict[letter] for letter in word]

print(phon_word)