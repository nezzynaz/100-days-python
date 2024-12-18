'''This script takes a name and then returns the name spelled out using the NATO alphabet'''

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
nato = {row.letter:row.code for (index, row) in df.iterrows()}
username = input("Type your name here:\n> ").upper()
parsed_name = [nato[letter] for letter in username]
print(parsed_name)
