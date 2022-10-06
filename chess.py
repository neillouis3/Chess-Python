def new_game():
    row8 = ('Rb', 'Nb', 'Bb', 'Qb', 'Kb', 'Bb', 'Nb', 'Rb')
    row7 = ('Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb', 'Pb')
    row6 = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    row5 = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    row4 = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    row3 = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    row2 = ('Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw', 'Pw')
    row1 = ('Rw', 'Nw', 'Bw', 'Qw', 'Kw', 'Bw', 'Nw', 'Rw')

    newBoard = ([row8, row7, row6, row5, row4, row3, row2, row1], "")
    turn = "W"

    return newBoard, turn


def print_game_state(b, turn):
    if turn.lower() == "b":
        print("It is Black's turn.")
    else:
        print("It is White's turn.")

    prettyBoard = ""
    row = 9
    rowinfo = "  a b c d e f g h  "

    for element in b[0]:
        string = ''
        for character in list(element):
            if character == " ":
                string += character.replace(" ", "□")
            elif 'b' in character:
                string += character.replace("b", "")
            elif 'w' in character:
                string += character.replace("w", "")

        row -= 1
        prettyBoard += str(row) + " " + " ".join(string) + \
            " " + str(row) + "\n"

    prettyBoard = rowinfo + '\n' + prettyBoard + rowinfo
    print(prettyBoard)
