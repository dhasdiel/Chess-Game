class Piece:

    def __init__(self, color):
        self.color = color

    def is_legal_move(self, from_square, to_square):
        """
        func check if move of piece is legal.
        param: 2 Square objects, first from where and the second to where.
        return: if move is legel return True else False 
        """
        raise NotImplementedError

    def get_piece_unicode_color(self):
        """
        func return unicode according to the color of the player.
        param: Piece object.
        return: the unicode color of piece like player color.
        """
        if self.color == "white":
            return 37
        elif self.color == "black":
            return 30
