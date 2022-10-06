def new_board():
    row8 = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    row7 = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    row6 = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    row5 = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    row4 = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    row3 = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    row2 = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    row1 = (' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')

    emptyBoard = [row8, row7, row6, row5, row4, row3, row2, row1]
    nothing = ""
    return emptyBoard, nothing


def colour(board, square):
    position = list(square)
    elementPosition = 8 - int(position[1])
    characterPosition = ord(position[0].lower()) - ord("a")

    pieceColor = None
    for i, element in enumerate(board[0]):
        if i == elementPosition:
            for j, character in enumerate(element):
                if j == characterPosition:
                    if "b" in character:
                        pieceColor = "B"
                    elif "w" in character:
                        pieceColor = "W"

    return pieceColor


def count_pieces(board, colour):
    count = 0
    for element in board[0]:
        for character in element:
            if colour.lower() in list(character):
                count += 1

    return count


def piece(board, square):
    position = list(square)
    elementPosition = 8 - int(position[1])
    characterPosition = ord(position[0].lower()) - ord("a")

    piece = ""
    for i, element in enumerate(board[0]):
        if i == elementPosition:
            for j, character in enumerate(element):
                if j == characterPosition:
                    if 'b' in character:
                        piece += character.replace("b", "")
                    elif 'w' in character:
                        piece += character.replace("w", "")
                    else:
                        return None
    return piece


def place_piece(board, square, colour, piece):
    position = list(square)
    elementPosition = 8 - int(position[1])
    characterPosition = ord(position[0].lower()) - ord("a")
    for i, element in enumerate(board[0]):
        if i == elementPosition:
            for j, character in enumerate(element):
                if j == characterPosition:
                    elementList = list(element)
                    elementList[j] = piece + colour.lower()
                    board[0][i] = tuple(elementList)


def pretty(board):
    prettyBoard = ""
    row = 9
    rowinfo = "  a b c d e f g h  "

    for element in board[0]:
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

    return prettyBoard
