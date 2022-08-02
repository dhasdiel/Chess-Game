from Move import Move


class GameControl:
    def __init__(self, board, white_player, black_player):
        self.board = board
        self.white_player = white_player
        self.black_player = black_player
        self.is_game_over = False

    def player_turn(self, player):
        """
        func get a input from the player and check if it is valid..
        param: Player object.
        return: valid input from the player. 
        """
        name = player.name
        while True:
            inputValue = input(f"{name}: Please enter your move: ")
            if len(inputValue) == 4 and (inputValue[0] >= "A" and inputValue[0] <= "H") \
                    and (inputValue[2] >= "A" and inputValue[2] <= "H") \
                    and (inputValue[1] >= "1" and inputValue[1] <= "8") \
                    and (inputValue[3] >= "1" and inputValue[3] <= "8"):
                return inputValue
            # print message "illegal move" in red
            print("\33[37;41millegal move\33[0m")

    def format_input(self, char):
        """
        func format the input from the player to index.
        param: a char from the input of the player.
        return: format the char to the right index. 
        """
        indexNums = ["8", "7", "6", "5", "4", "3", "2", "1"]
        indexLetters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        if char >= "A" and char <= "H":
            return indexLetters.index(char)
        elif char >= "1" and char <= "8":
            return indexNums.index(char)

    def is_mate(self, king_square, player, board):
        """
        func check if player on mate.
        params: 
        change: if king is in mate change the variable "is_game_over" to True.
        return: None. 
        """
        mat = board.mat
        mate = True
        move = None
        # check col -1
        if king_square.col-1 >= 0:
            move = Move(king_square, mat[king_square.row]
                        [king_square.col-1], player, board)
            if not move.is_piece_get_block() and not player.is_check(None, mat[king_square.row][king_square.col-1], board):
                mate = False
        # check col +1
        if king_square.col+1 <= 7:
            move = Move(king_square, mat[king_square.row]
                        [king_square.col+1], player, board)
            if not move.is_piece_get_block() and not player.is_check(None, mat[king_square.row][king_square.col+1],  board):
                mate = False
        # check rows
        for col in range(king_square.col-1, king_square.col+1):
            # check row -1
            if king_square.row-1 >= 0:
                move = Move(
                    king_square, mat[king_square.row-1][col], player, board)
                if not move.is_piece_get_block() and not player.is_check(None, mat[king_square.row-1][col],  board):
                    mate = False
            # check row +1
            if king_square.row+1 <= 7:
                move = Move(
                    king_square, mat[king_square.row+1][col], player, board)
                if not move.is_piece_get_block() and not player.is_check(None, mat[king_square.row+1][col], board):
                    mate = False

        if mate:
            self.is_game_over = True

    def is_checkmate(self, player):
        """
        func check if it can be checkmate.
        params: GameControl object and the player in that turn.
        print: if is_check is true print warnning message.
        return: None. 
        """
        mat = self.board.mat
        king_square = self.board.find_king_square(player.color)
        for row in range(self.board.size):
            for col in range(self.board.size):
                square = mat[row][col]
                if square.piece == " ":
                    continue
                if square.piece.color == player.color:
                    continue
                if player.is_check(square, king_square, self.board):
                    # print warnning message to player in yellow
                    print(f"\33[30;43m{player.name} you are on check!\33[0m")
                    # player.on_check = True
                    self.is_mate(king_square, player, self.board)

    def handle_winner(self, players):
        """
        func check which player is "on_check" equal to False.
        param: GameControl object, list of the players.
        print: The player who won. 
        """
        for player in players:
            if not player.on_check:
                print(f"{player.name} won!")

    def start_game(self):
        """
        func start the game.
        param: GameControl object.
        return: None. 
        """
        board = self.board
        players = [self.white_player, self.black_player]
        print("\33[2J")  # clean screen
        board.init_board()
        while not self.is_game_over:
            for player in players:
                invalid_input = True
                self.is_checkmate(player)
                board.print_board()
                if self.is_game_over:
                    break
                while invalid_input:
                    formatMove = self.player_turn(player)
                    move = Move(board.mat[self.format_input(formatMove[1])][self.format_input(formatMove[0])],
                                board.mat[self.format_input(formatMove[3])][self.format_input(formatMove[2])], player, board)
                    if move.make_move() and not player.on_check:
                        invalid_input = False
        self.handle_winner(players)
