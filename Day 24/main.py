
with open("./Input/Names/invited_names.txt", "r") as name_file:
    names_list = name_file.readlines()
with open("./Input/Letters/starting_letter.txt", "r") as starting_letter:
    starting_letter_list = starting_letter.readlines()


for name in names_list:
    name = name.strip()
    message = starting_letter_list.copy()
    message[0] = starting_letter_list[0].replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_to_{name}", mode="w") as f:
        f.writelines(message)


