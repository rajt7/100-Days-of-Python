with open("../Input/Letter/letter.txt", "r") as letter_file:
    letter = letter_file.read()

    with open("../Input/Invitation_list/names.txt", "r") as invitation_file:
        names = invitation_file.readlines()

        for name in names:
            name = name.replace("\n", "")
            new_letter = letter.replace("{name}", name)

            with open(f"./ready_to_send/letter_for_{name}.txt", "w") as ready_file:
                ready_file.write(new_letter)