from Piece import Piece


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        self.unicode = "\u265F"

    def is_legal_move(self, from_square, to_square):
        """
        func check if move of piece is legal.
        param: 2 Square objects, first from where and the second to where.
        return: if move is legel return True else False 
        """
        if to_square.row < 0 or to_square.row > 7 \
                or to_square.col < 0 or to_square.col > 7:
            return False
        # case pawn color is "white"
        elif self.color == "white":
            if from_square.col == to_square.col and from_square.row == to_square.row+1 and to_square.piece == " ":
                return True
            elif from_square.row == 6 and from_square.col == to_square.col and \
                    (from_square.row == to_square.row+2 or from_square.row == to_square.row+1):
                return True
            elif to_square.piece != " " and from_square.row == to_square.row+1 and \
                    (from_square.col == to_square.col+1 or from_square.col == to_square.col - 1):
                return True
            else:
                return False
        # cse pawn color is "black"
        elif self.color == "black":
            if from_square.col == to_square.col and from_square.row == to_square.row-1 and to_square.piece == " ":
                return True
            elif from_square.row == 1 and from_square.col == to_square.col and \
                    (from_square.row == to_square.row-2 or from_square.row == to_square.row-1):
                return True
            elif to_square.piece != " " and from_square.row == to_square.row-1 and \
                    (from_square.col == to_square.col-1 or from_square.col == to_square.col + 1):
                return True
            else:
                return False
