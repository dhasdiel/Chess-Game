from Board import Board
from GameControl import GameControl
from Player import Player


white_player = Player(input("Enter white player name: "), "white")
white_player.check_name()
black_player = Player(input("Enter black player name: "), "black")
black_player.check_name()

game = GameControl(Board(), white_player, black_player)
game.start_game()
