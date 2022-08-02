from Move import Move


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.on_check = False

    def check_name(self):
        """
        func check the name of the player and check if it is valid.
        param: Player object.
        return: None. 
        """
        while self.name == "" or self.name == " ":
            self.name = input("Enter your name again: ")
        return

    def is_check(self, from_square, king_square, board):
        """
        func get a input from the player and check if it is valid..
        param: 2 Square objects, the first square from where to go the second square...
        return: if square is check on king square return True else False.
        """
        if not from_square:
            for row in range(board.size):
                for col in range(board.size):
                    square = board.mat[row][col]
                    if square.piece == " ":
                        continue
                    if square.piece.color == self.color:
                        continue
                    move = Move(square, king_square, self, board)
                    if square.piece.is_legal_move(square, king_square) and not move.is_piece_get_block():
                        self.on_check = True
                        return True

        else:
            move = Move(from_square, king_square, self, board)
            if from_square.piece.is_legal_move(from_square, king_square) and not move.is_piece_get_block():
                self.on_check = True
                return True

        return False
