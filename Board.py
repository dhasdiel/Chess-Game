from Square import Square
from Pieces.Rook import Rook
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Pawn import Pawn


class Board:
    def __init__(self):
        self.size = 8
        self.mat = []

    def init_pieces(self, color):
        """
        func create the pieces on the board according to the color.
        param: Board object and string color.
        return: None.
        """
        index = 7 if color == "white" else 0
        # rooks
        self.mat[index][0].piece = Rook(color)
        self.mat[index][7].piece = Rook(color)
        # knights
        self.mat[index][1].piece = Knight(color)
        self.mat[index][6].piece = Knight(color)
        # bishops
        self.mat[index][2].piece = Bishop(color)
        self.mat[index][5].piece = Bishop(color)
        # queen
        self.mat[index][3].piece = Queen(color)
        # king
        self.mat[index][4].piece = King(color)
        # pawns
        pawn_index = 6 if index == 7 else 1
        for i in range(self.size):
            self.mat[pawn_index][i].piece = Pawn(color)

    def init_board(self):
        """
        func create the mat of the board.
        param: Board object.
        return: None.
        """
        for i in range(self.size):
            board_row = []
            for j in range(self.size):
                square = Square(i, j, " ")
                board_row.append(square)
            self.mat.append(board_row)
        self.init_pieces("white")
        self.init_pieces("black")

    def print_letters(self):
        """
        func print the letters on board.
        param: Board object.
        return: None.
        """
        print("    ", end="")
        for c in range(self.size):
            print(chr(65 + c) + "  ", end="")
        print()

    def print_bgcolor(self, square):
        """
        func print the background color of the square.
        param: Board object and Square object.
        return: None.
        """
        bg_azure = 46
        bg_green = 42
        piece_color = 30
        text = square.piece.unicode if square.piece != " " else " "
        if text != " ":
            piece_color = square.piece.get_piece_unicode_color()
        if square.row % 2 == 0:
            if square.col % 2 == 0:
                print(
                    f"\33[{piece_color};{bg_azure}m {text} \33[0m", end="")
            else:
                print(
                    f"\33[{piece_color};{bg_green}m {text} \33[0m", end="")
        else:
            if square.col % 2 == 0:
                print(
                    f"\33[{piece_color};{bg_green}m {text} \33[0m", end="")
            else:
                print(
                    f"\33[{piece_color};{bg_azure}m {text} \33[0m", end="")

    def print_board(self):
        """
        func print the board of the game.
        param: Board object.
        return: None.
        """
        self.print_letters()
        for i in range(self.size):
            print(f" {self.size - i} ", end="")
            for j in range(self.size):
                self.print_bgcolor(self.mat[i][j])
            print(f" {self.size - i} ", end="")
            print()
        self.print_letters()

    def find_king_square(self, color):
        """
        func find the square according to the color of the player.
        param: Board object and color of the player.
        return: the square that the king is on it and same color as the player.
        """
        king_piece = King(color)
        king_square = None
        for row in range(self.size):
            for col in range(self.size):
                if self.mat[row][col].piece == " ":
                    continue
                if not isinstance(self.mat[row][col].piece, King):
                    continue
                if self.mat[row][col].piece.color == king_piece.color:
                    king_square = self.mat[row][col]
                # if self.mat[row][col].piece != " " and self.mat[row][col].piece.unicode == king_piece.unicode and \
                #         self.mat[row][col].piece.color == king_piece.color:
                #     king_square = self.mat[row][col]
        return king_square
