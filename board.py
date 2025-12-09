import pygame
from math import sqrt

from constants import *

# ------------------------------------

class Board():
    def __init__(self):
        # Create the 3x3 board
        self.board = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "null"]
        # board = [
        #     [(0, 0), (1, 0), (2, 0)],
        #     [(0, 1), (1, 1), (2, 1)],
        #     [(0, 2), (1, 2), (2, 2)]
        # ]
        self.tile_centers = []

    # Draw the board to the screen
    def draw(self):
        # Draw vertical lines
        lines_start_end_v = []

        for i in range(4):
            start_pos_x = screen_center[0] - int(3 * tile_width / 2) + (i * tile_width)
            start_pos_y = screen_center[1] - int(3 * tile_width / 2)
            start_pos = (start_pos_x, start_pos_y)

            end_pos_x = start_pos_x
            end_pos_y = screen_center[1] + int(3 * tile_width / 2)
            end_pos = (end_pos_x, end_pos_y)

            lines_start_end_v.append([start_pos, end_pos])

        # Draw horizontal lines
        lines_start_end_h = []

        for j in range(4):
            start_pos_x = screen_center[0] - int(3 * tile_width / 2)
            start_pos_y = screen_center[1] - int(3 * tile_width / 2) + (j * tile_width)
            start_pos = (start_pos_x, start_pos_y)

            end_pos_x = screen_center[0] + int(3 * tile_width / 2)
            end_pos_y = start_pos_y
            end_pos = (end_pos_x, end_pos_y)

            lines_start_end_h.append([start_pos, end_pos])

        # Append tile centers
        for i in range(3):
            y = screen_center[1] - tile_width + tile_width * i
            for j in range(3):
                tile_center = [screen_center[0] - tile_width + (tile_width * j), y]
                self.tile_centers.append(tile_center)

        return [lines_start_end_v, lines_start_end_h]
    
    # Get the nearest tile to a mouse click location
    def get_nearest_tile(self, mouse_pos):
        if mouse_pos[0] > (screen_center[0] - int(3 * tile_width / 2)) and mouse_pos[0] < (screen_center[0] + int(3 * tile_width / 2)) and mouse_pos[1] > (screen_center[1] - int(3 * tile_width / 2)) and mouse_pos[1] < (screen_center[1] + int(3 * tile_width / 2)):
            _distance = 1000
            nearest_tile_index = 0 # Initializes to the first tile

            # Checks how far away the mouse position is from the center of each tile
            for center in self.tile_centers:
                tile_index = self.tile_centers.index(center) # Index of current tile

                distance = sqrt(pow((mouse_pos[1]) - (center[1]), 2) + pow((mouse_pos[0]) - (center[0]), 2)) # Distance formula

                if distance < _distance:
                    _distance = distance
                    nearest_tile_index = tile_index

            # Return the index of the closest tile to the mouse position
            return nearest_tile_index
        else:
            return -1
    
    # Return the coordinates of the given tile center
    def get_tile_center(self, tile_index):
        return self.tile_centers[tile_index]
    
    # Check if a tile is empty
    def get_tile_status(self, tile_index):
        if self.board[tile_index] == "_":
            return True
        return False
    
    # Sets the tile status to filled if it is empty (does not need to work backwards since players don't take their pieces back)
    def set_tile_status(self, tile_index, char):
        if self.get_tile_status(tile_index):
            self.board[tile_index] = char
            return True
        return False

        # print(self.board)

    # Check the board for a win
    def check_win(self, pieces, color, player):
        if len(pieces) >= 3:
            for i in range(len(pieces)):
                # Check from tile zero
                if pieces[i] == 0:
                    # Check for a win in a row
                    if pieces[i] + 1 in pieces and pieces[i] + 2 in pieces:
                        player.score += 1
                        return [True, color]
                    # Check for a win in a column
                    if pieces[i] + 3 in pieces and pieces[i] + 6 in pieces:
                        player.score += 1
                        return [True, color]
                    # Check for a win in a diagonal
                    if pieces[i] + 4 in pieces and pieces[i] + 8 in pieces:
                        player.score += 1
                        return [True, color]
                
                # Check from tile 3
                elif pieces[i] == 3:
                    # Check for a win in a row
                    if pieces[i] + 1 in pieces and pieces[i] + 2 in pieces:
                        player.score += 1
                        return [True, color]
                    
                # Check from tile 6
                elif pieces[i] == 6:
                    # Check for a win in a row
                    if pieces[i] + 1 in pieces and pieces[i] + 2 in pieces:
                        player.score += 1
                        return [True, color]
                    # Check for a win in a diagonal
                    if pieces[i] - 2 in pieces and pieces[i] - 4 in pieces:
                        player.score += 1
                        return [True, color]
                    
                # Check from tile 1
                elif pieces[i] == 1:
                    # Check for a win in a column
                    if pieces[i] + 3 in pieces and pieces[i] + 6 in pieces:
                        player.score += 1
                        return [True, color]
                    
                # Check from tile 2
                elif pieces[i] == 2:
                    # Check for a win in a column
                    if pieces[i] + 3 in pieces and pieces[i] + 6 in pieces:
                        player.score += 1
                        return [True, color]
                    
            return [False, ""]
        return [False, ""]
    
    def check_tie(self):
        if self.board == ["x", "x", "x", "x", "x", "x", "x", "x", "x", "null"]:
            return [True, "Nobody"]
        return [False, ""]