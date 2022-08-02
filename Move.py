import copy
from Pieces.Knight import Knight
from Pieces.Pawn import Pawn
from Pieces.Queen import Queen


class Move:
    def __init__(self, from_square, to_square, player, board):
        self.from_square = from_square
        self.to_square = to_square
        self.player = player
        self.board = board

    def check_col_get_block(self):
        """
        func check when piece move on col can be block by other piece.
        param: Move object.
        return: True if move can be block by other piece else False. 
        """
        op_row = None
        if self.from_square.row < self.to_square.row:
            # go down on board
            op_row = "+"
        else:
            # go up on board
            op_row = "-"

        for i in range(1, abs(self.from_square.row-self.to_square.row) + 1):
            # exmple: self.from_square.row = 4, op_row = "+" and i = 2
            # so eval(4+2) make a int 6 that means row = 6
            row = eval(str(self.from_square.row)+op_row+str(i))
            square = self.board.mat[row][self.from_square.col]
            if square.piece != " ":
                return square
        return False

    def check_row_get_block(self):
        """
        func check when piece move on row can be block by other piece.
        param: Move object.
        return: True if move can be block by other piece else False. 
        """
        op_col = None
        if self.from_square.col > self.to_square.col:
            # go left on the coard
            op_col = "-"
        else:
            # go right on the coard
            op_col = "+"

        for i in range(1, abs(self.from_square.col-self.to_square.col) + 1):
            # exmple: self.from_square.col = 4, op_col = "+" and i = 2
            # so eval(4+2) make a int 6 that means col = 6
            col = eval(str(self.from_square.col)+op_col+str(i))
            square = self.board.mat[self.from_square.row][col]
            if square.piece != " ":
                return square
        return False

    def check_diagonals_get_block(self):
        """
        func check when piece move on diagonal can be block by other piece.
        param: Move object.
        return: True if move can be block by other piece else False. 
        """
        op_row = None
        op_col = None
        if self.from_square.row > self.to_square.row:
            # go up on board
            op_row = "-"
            if self.from_square.col < self.to_square.col:
                # go up and right on board
                op_col = "+"
            else:
                # go up and left on board
                op_col = "-"
        else:
            # go down on board
            op_row = "+"
            if self.from_square.col < self.to_square.col:
                # go down and right on board
                op_col = "+"
            else:
                # go down and left on board
                op_col = "-"

        for i in range(1, abs(self.from_square.row - self.to_square.row)+1):
            # exmple: self.from_square.row = 4, op_row = "+" and i = 2
            # so eval(4+2) make a int 6 that means row = 6. same for col
            row = eval(str(self.from_square.row)+op_row+str(i))
            col = eval(str(self.from_square.col)+op_col+str(i))
            square = self.board.mat[row][col]
            if square.piece != " ":
                return square
        return False

    def is_piece_get_block(self):
        """
        func check when piece move on board can be block by other piece.
        param: Move object.
        return: True if move can be block by other piece else False. 
        """
        block_square = None
        if isinstance(self.from_square.piece, Knight):
            return False

        elif self.from_square.row == self.to_square.row:
            block_square = self.check_row_get_block()

        elif self.from_square.col == self.to_square.col:
            block_square = self.check_col_get_block()
        else:
            block_square = self.check_diagonals_get_block()

        if block_square:
            if not self.from_square.is_square_piece_same_color(block_square):
                if self.to_square.is_square_same_row_and_col(block_square):
                    return False
                return True
            else:
                return True

        return False

    def move_cause_check(self):
        """
        func check if move can cause check.
        param: Move object.
        return: True if move cause check else False. 
        """
        clone_board = copy.deepcopy(self.board)
        from_square = clone_board.mat[self.from_square.row][self.from_square.col]
        to_square = clone_board.mat[self.to_square.row][self.to_square.col]
        to_square.piece = from_square.piece
        from_square.piece = " "
        if self.player.is_check(None, clone_board.find_king_square(self.player.color), clone_board):
            return True
        return False

    def make_move(self):
        """
        func check if move can exist.
        param: Move object.
        return: True if move can exit else False. 
        """
        # illegal move when the player try to move the same square
        if self.from_square == self.to_square:
            # print message "illegal move" in red
            print("\33[37;41millegal move\33[0m")
            return False

        elif self.from_square.piece == " ":
            # print message "illegal move" in red
            print("\33[37;41millegal move\33[0m")
            return False

        elif self.is_piece_get_block():
            print("\33[37;41millegal move\33[0m")
            return False

        elif self.move_cause_check():
            print("\33[37;41millegal move\33[0m")
            return False

        # llegal move
        elif self.from_square.piece.is_legal_move(self.from_square, self.to_square) \
                and self.from_square.piece.color == self.player.color:
            self.to_square.piece = self.from_square.piece
            self.from_square.piece = " "
            # in case of pawn get in the last raw change the pawn to queen
            if isinstance(self.to_square.piece, Pawn) and (self.to_square.row == 0 or self.to_square.row == 7):
                new_queen = Queen(self.to_square.piece.color)
                self.to_square.piece = new_queen
            # if self.player.on_check:
            self.player.on_check = False
            return True

        else:
            # print message "illegal move" in red
            print("\33[37;41millegal move\33[0m")
            return False
