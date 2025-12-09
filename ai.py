import pygame
from time import sleep
from random import shuffle, choice

from constants import *
from helpers import *

from player import Player

# 
class AIPlayer(Player):
	def __init__(self, color):
		super().__init__(color)

    # AI helper functions
	def check_move_win(self, index, curr_board, pieces):
		if len(pieces) > 2:
			# Make the move and check its result
			curr_board.insert(index, self.char)
			pieces.append(index)

			# Check for a win
			result = check_win(pieces, "BLUE", self)
			if result[0]:
				# If it did not win or block the opponent
				curr_board.pop(index)
				pieces.remove(index)
				return result[0]
		
	def pick_tile(self, curr_board):
		if curr_board[4] == "_":
			return 4
		else:
			corners = [0, 2, 6, 8]
			corners_available = []
			for index, tile in enumerate(curr_board):
				if index in corners and tile == "_":
					corners_available.append(index)

			return choice(corners_available)

	# Overall function to make a move for AI
	def make_move(self, board, player_pieces):
		curr_board = board
		curr_pieces = player_pieces

		# Check for win
		for index, tile in enumerate(curr_board):
			if tile == "_":
				
				if self.check_move_win(index, curr_board, curr_pieces):
					self.pieces.append(index)
					return index
				else:
					index = self.pick_tile(curr_board)
					self.pieces.append(index)
					return index