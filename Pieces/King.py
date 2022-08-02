from Piece import Piece


class King(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.unicode = "\u265A"

    def is_legal_move(self, from_square, to_square):
        """
        func check if move of piece is legal.
        param: 2 Square objects, first from where and the second to where.
        return: if move is legel return True else False 
        """
        if from_square.row == to_square.row:
            if from_square.col == to_square.col + 1 or from_square.col == to_square.col - 1:
                return True
        elif from_square.row == to_square.row-1:
            if from_square.col == to_square.col + 1 or from_square.col == to_square.col - 1 \
                    or from_square.col == to_square.col:
                return True
        elif from_square.row == to_square.row+1:
            if from_square.col == to_square.col + 1 or from_square.col == to_square.col - 1 \
                    or from_square.col == to_square.col:
                return True
        else:
            return False
