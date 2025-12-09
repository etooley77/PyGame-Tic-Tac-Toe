import pygame

from constants import *

from player import Player

# 
class AIPlayer(Player):
	def __init__(self, color):
		super().__init__(color)

    # AI helper functions
	def check_move(self):
		# Make the move and check its result
		pass

	# Overall function to make a move for AI
	def make_move(self, board, player_pieces):
		curr_board = board
		for index, tile in enumerate(curr_board):
			if tile == "_":
				self.check_move(index)

				# CREATE A HELPER FUNCTION FILE FOR FUNCTIONS SUCH AS CHECK WIN, INSTEAD OF ABSTRACTING IT INTO THE BOARD CLASS ALONE!