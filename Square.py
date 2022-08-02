class Square:
    def __init__(self, row, col, piece):
        self.row = row
        self.col = col
        self.piece = piece

    def is_square_piece_same_color(self, second_square):
        """
        func check if square and other square pieces have same color.
        param: 2 Square objects.
        return: True if same color else False. 
        """
        if second_square.piece != " ":
            if self.piece.color == second_square.piece.color:
                return True
        return False

    def is_square_same_row_and_col(self, second_square):
        """
        func check if squares have same rows and cols.
        param: 2 Square objects.
        return: True if same rows and cols else False.
        """
        if self.row == second_square.row and self.col == second_square.col:
            return True
        return False
