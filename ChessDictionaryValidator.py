def is_valid_chess_board(board):
    valid_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']  # array with valid position letters
    valid_pieces = ['king', 'queen', 'bishop', 'knight', 'rook', 'pawn']  # array with chess piece types
    black_pieces = 0
    white_pieces = 0
    total_pieces = 0
    bpawns = 0
    wpawns = 0
    bking = 0
    wking = 0
    # the above code and variables may be shortened by the use of a dictionary (unfortunately not fluent enough in them)

    # validating chess piece positions and quantity
    for position in board.keys():
        total_pieces += 1
        if int(position[0]) < 1 or int(position[0]) > 8:
            return "Improper Chess Board: Position " + position + " exceeds board limit (<1 or >8)"
        elif position[1] not in valid_letters:
            return "Improper Chess Board: Position " + position + " exceeds board limit (>h)"
        elif total_pieces > 16:
            return "Improper Chess Board: Over 16 pieces on the board"

    for piece in board.values():
        # validating chess piece names
        if piece[0] != 'b' and piece[0] != 'w':
            return "Improper Chess Board: Piece " + piece + " is neither black or white"
        elif piece[1:] not in valid_pieces:
            return "Improper Chess Board: Piece " + piece + " is not a valid chess piece"

        # validating chess piece quantity by color
        if piece[0] == 'b':
            black_pieces += 1
            if black_pieces > 16:
                return "Improper Chess Board: Over 16 black pieces"
        elif piece[0] == 'w':
            white_pieces += 1
            if white_pieces > 16:
                return "Improper Chess Board: Over 16 white pieces"

        # validating quantity of kings and pawns
        if piece == 'bking':
            bking += 1
            if bking > 1:
                return "Improper Chess Board: More than 1 Black King piece"
        elif piece == 'wking':
            wking += 1
            if wking > 1:
                return "Improper Chess Board: More than 1 White King piece"
        elif piece == 'bpawn':
            bpawns += 1
            if bpawns > 8:
                return "Improper Chess Board: More than 8 Black Pawn pieces"
        elif piece == 'wpawn':
            wpawns += 1
            if wpawns > 8:
                return "Improper Chess Board: More than 8 White Pawn pieces"

        return "Valid Chess Board"


try_board = {'2h': 'bking', '3b': 'bpawn', '2a': "wking"}
print(is_valid_chess_board(try_board))
