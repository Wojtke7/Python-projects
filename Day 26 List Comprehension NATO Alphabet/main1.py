#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")

letters_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# print(letters_dict)

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Type word to convert into NATO alphabet: ").upper()
output_list = [letters_dict[letter] for letter in word]
print(output_list)
