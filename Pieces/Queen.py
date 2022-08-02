from Piece import Piece


class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.unicode = "\u265B"

    def is_legal_move(self, from_square, to_square):
        """
        func check if move of piece is legal.
        param: 2 Square objects, first from where and the second to where.
        return: if move is legel return True else False 
        """
        if abs(from_square.row - to_square.row) == abs(from_square.col - to_square.col):
            return True
        elif from_square.row == to_square.row or from_square.col == to_square.col:
            return True
        else:
            return False
