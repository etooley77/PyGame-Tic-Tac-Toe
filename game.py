import pygame
import sys
from time import sleep

from constants import *
from helpers import *

from board import Board
from piece import Piece
from player import Player
from ai import AIPlayer

# ---------------------------------------------------

class Game():
    def __init__(self):
        # Initialize pygame
        pygame.init()
        self.game_clock = pygame.time.Clock()

        # Screen setup
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Tic-Tac-Toe")

        # Game start
        self.game_started = False

        # Font, images, and sounds
        self.font80 = pygame.font.SysFont("Arial", 80, bold=True)
        self.font40 = pygame.font.SysFont("Arial", 40, bold=True)
        self.font20 = pygame.font.SysFont("Arial", 20, bold=True)

        self.icon = pygame.image.load("assets/icon.ico").convert_alpha()
        pygame.display.set_icon(self.icon) # Set icon

        self.home_image = pygame.image.load("assets/home.png").convert_alpha()

        # Board setup
        self.board = Board()
        self.lines = self.board.draw()

        # Piece handling
        self.pieces = pygame.sprite.Group()

        # Players
        self.p1 = Player(RED)
        self.p2 = None
        self.curr_move = 1

        self.turn = "RED"

        # Check for game win
        self.game_won = False
        self.winner = ""
        self.last_winner = ""

    # 
    # Screen functions
    # 
    
    # Draw the screen
    def draw_start_screen_frame(self):
        # mouse_pos = pygame.mouse.get_pos()

        # Fill the screen with black
        self.screen.fill(BLACK)

        title_center_y = (screen_height / 2) - (screen_height / 3)
        instructions_center_y = (screen_height / 2) + (screen_height / 3)

        # Title
        title = self.font80.render(f"Tic-Tac-Toe", True, WHITE)
        self.screen.blit(title, ((screen_width / 2) - (title.get_width() / 2), title_center_y))

        # Local multiplayer
        local_instructions = self.font40.render(f"Press '1' to play local", True, WHITE)
        self.screen.blit(local_instructions, ((screen_width / 2) - (local_instructions.get_width() / 2), instructions_center_y - local_instructions.get_height() / 2))

        # Button test
        # local_button = [(screen_width / 2) - (screen_width / 3), 3 * (screen_height / 4), (screen_width / 4), (screen_height / 12)]

        # if mouse_pos[0] > local_button[0] and mouse_pos[0] < local_button[0] + local_button[2] and mouse_pos[1] > local_button[1] and mouse_pos[1] < local_button[1] + local_button[3]:
        #     local_border_width = 0
        # else:
        #     local_border_width = 5

        # pygame.draw.rect(self.screen, GRAY, local_button, local_border_width)

        # Play AI
        ai_instructions = self.font40.render(f"Press '2' to play AI", True, WHITE)
        self.screen.blit(ai_instructions, ((screen_width / 2) - (ai_instructions.get_width() / 2), instructions_center_y + local_instructions.get_height() / 2))

        # Button test
        # ai_button = [(screen_width / 2), 3 * (screen_height / 4), (screen_width / 4), (screen_height / 12)]

        # if mouse_pos[0] > ai_button[0] and mouse_pos[0] < ai_button[0] + ai_button[2] and mouse_pos[1] > ai_button[1] and mouse_pos[1] < ai_button[1] + ai_button[3]:
        #     ai_border_width = 0
        # else:
        #     ai_border_width = 5

        # pygame.draw.rect(self.screen, GRAY, ai_button, ai_border_width)

        # Home screen image
        self.screen.blit(self.home_image, self.home_image.get_rect(center = screen_center))

    # Start screen loop
    def start_screen(self):
        for event in pygame.event.get():
            # Handle quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle game start event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.game_started = True
                    self.p2 = Player(BLUE)
                elif event.key == pygame.K_2:
                    self.game_started = True
                    self.p2 = AIPlayer(BLUE)
        
        self.draw_start_screen_frame()

        # Update the display
        pygame.display.flip()
        self.game_clock.tick(60)

    def round_screen(self):
        for event in pygame.event.get():
            # Handle quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle keydown events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print(self.board.board)
            # Handle mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.game_won:
                    # Find the nearest tile and check if it is empty
                    coords = pygame.mouse.get_pos()
                    nearest_tile = self.board.get_nearest_tile(coords)
                    
                    # If empty
                    if self.board.get_tile_status(nearest_tile):
                        # If p1's turn
                        if self.turn == "RED":
                            # Mark tile as covered
                            if self.board.set_tile_status(nearest_tile, self.p1.char):
                                # Create new piece with p1's color
                                new_piece = Piece(self.p1.color, self.board.get_tile_center(nearest_tile), nearest_tile)
                                self.p1.pieces.append(nearest_tile)
                                self.pieces.add(new_piece)

                                self.curr_move += 1 # Next move

                                check_result = check_win(self.p1.pieces, "RED", self.p1) # Check for win
                                if check_result[0]:
                                    self.game_won = check_result[0]
                                    self.winner = check_result[1]
                                else:
                                    # Check for a tie
                                    tie_check_result = check_tie(self.board.board)
                                    self.game_won = tie_check_result[0]
                                    self.winner = tie_check_result[1]

                                self.turn = "BLUE"
                        # if p2's turn
                        else:
                            # Mark tile as covered
                            if self.board.set_tile_status(nearest_tile, self.p2.char):
                                # Create new piece with p2's color
                                new_piece = Piece(self.p2.color, self.board.get_tile_center(nearest_tile), nearest_tile)
                                self.p2.pieces.append(nearest_tile)
                                self.pieces.add(new_piece)

                                self.curr_move += 1 # Next move

                                check_result = check_win(self.p2.pieces, "BLUE", self.p2) # Check for win
                                if check_result[0]:
                                    self.game_won = check_result[0]
                                    self.winner = check_result[1]
                                else:
                                    # Check for a tie
                                    tie_check_result = check_tie(self.board.board)
                                    self.game_won = tie_check_result[0]
                                    self.winner = tie_check_result[1]

                                self.turn = "RED"

                    # print(f"Mouse button clicked at {coords} --- nearest to the tile at index {nearest_tile}")

        # Clear the screen
        self.screen.fill(BLACK)

        # Display the score
        p1_score = self.font20.render(f"RED: {self.p1.score}", True, WHITE)
        p2_score = self.font20.render(f"BLUE: {self.p2.score}", True, WHITE)

        self.screen.blit(p1_score, (10, 10))
        self.screen.blit(p2_score, (10, 30))

        # Display the turn
        turn = self.font40.render(f"{self.turn}'s turn", True, WHITE)
        self.screen.blit(turn, (screen_width / 2 - 75, 15))

        # Draw all of the vertical and horizontal lines onto the screen
        for line in self.lines[0]:
            pygame.draw.line(self.screen, WHITE, line[0], line[1], 1)

        for line in self.lines[1]:
            pygame.draw.line(self.screen, WHITE, line[0], line[1], 1)

        # Draw pieces
        for piece in self.pieces:
            self.screen.blit(piece.surface, piece.rect)

        # Update the display
        pygame.display.flip()
        self.game_clock.tick(60)

    def ai_round_screen(self):
        for event in pygame.event.get():
            # Handle quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Handle keydown events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print(self.board.board)
            # Handle mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.game_won:
                    # Find the nearest tile and check if it is empty
                    coords = pygame.mouse.get_pos()
                    nearest_tile = self.board.get_nearest_tile(coords)
                    
                    # If empty
                    if self.board.get_tile_status(nearest_tile):
                        # If p1's turn
                        if self.turn == "RED":
                            # Mark tile as covered
                            if self.board.set_tile_status(nearest_tile, self.p1.char):
                                # Create new piece with p1's color
                                new_piece = Piece(self.p1.color, self.board.get_tile_center(nearest_tile), nearest_tile)
                                self.p1.pieces.append(nearest_tile)
                                self.pieces.add(new_piece)

                                self.curr_move += 1 # Next move

                                check_result = self.board.check_win(self.p1.pieces, "RED", self.p1) # Check for win
                                if check_result[0]:
                                    self.game_won = check_result[0]
                                    self.winner = check_result[1]
                                else:
                                    # Check for a tie
                                    tie_check_result = self.board.check_tie()
                                    self.game_won = tie_check_result[0]
                                    self.winner = tie_check_result[1]

                                self.turn = "BLUE"
                        # if p2's turn
                        else:
                            # Check moves
                            move_index = self.p2.make_move(self.board)

                            new_piece = Piece(self.p2.color, self.board.get_tile_center(move_index), move_index)
                            self.p1.pieces.append(move_index)
                            self.pieces.add(new_piece)

                            self.curr_move += 1 # Next move

                            check_result = self.board.check_win(self.p2.pieces, "BLUE", self.p2) # Check for win
                            if check_result[0]:
                                self.game_won = check_result[0]
                                self.winner = check_result[1]
                            else:
                                # Check for a tie
                                tie_check_result = self.board.check_tie()
                                self.game_won = tie_check_result[0]
                                self.winner = tie_check_result[1]

                            self.turn = "RED"

                    # print(f"Mouse button clicked at {coords} --- nearest to the tile at index {nearest_tile}")

        # Clear the screen
        self.screen.fill(BLACK)

        # Display the score
        p1_score = self.font20.render(f"RED: {self.p1.score}", True, WHITE)
        p2_score = self.font20.render(f"BLUE: {self.p2.score}", True, WHITE)

        self.screen.blit(p1_score, (10, 10))
        self.screen.blit(p2_score, (10, 30))

        # Display the turn
        turn = self.font40.render(f"{self.turn}'s turn", True, WHITE)
        self.screen.blit(turn, (screen_width / 2 - 75, 15))

        # Draw all of the vertical and horizontal lines onto the screen
        for line in self.lines[0]:
            pygame.draw.line(self.screen, WHITE, line[0], line[1], 1)

        for line in self.lines[1]:
            pygame.draw.line(self.screen, WHITE, line[0], line[1], 1)

        # Draw pieces
        for piece in self.pieces:
            self.screen.blit(piece.surface, piece.rect)

        # Update the display
        pygame.display.flip()
        self.game_clock.tick(60)

    def win_screen(self):
        for event in pygame.event.get():
            # Handle quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Restart event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.screen.fill(BLACK)

                    # Remove all pieces
                    self.board.board = ["_", "_", "_", "_", "_", "_", "_", "_", "_", "null"]

                    self.p1.pieces = []
                    self.p2.pieces = []
                    
                    for piece in self.pieces.sprites():
                        piece.kill()
                    
                    # Reset the move count and turn
                    self.curr_move = 1

                    if self.winner == "RED":
                        self.last_winner = "RED"
                        self.turn = "BLUE"
                    elif self.winner == "BLUE":
                        self.last_winner = "BLUE"
                        self.turn = "RED"
                    else:
                        if self.last_winner == "RED":
                            self.turn = "BLUE"
                        else:
                            self.turn = "RED"

                    # Reset the win boolean and the winner
                    self.game_won = False
                    self.winner = ""

        # Clear the screen
        self.screen.fill(BLACK)

        # Display who has won
        win_statement = self.font40.render(f"{self.winner} won!", True, WHITE)
        self.screen.blit(win_statement, (screen_width / 2 - 50, screen_height / 2 - 20))

        reset_statement = self.font20.render(f"Press 'r' to play again", True, WHITE)
        self.screen.blit(reset_statement, (screen_width / 2 - 50, screen_height / 2 + 20))

        # Update the display
        pygame.display.flip()
        self.game_clock.tick(60)



    # Game Loop
    def run(self):
        while not self.game_won and not self.game_started:
            self.start_screen()

        # Main game loop
        while not self.game_won and self.game_started:
            self.round_screen()

        # When a player has won
        while self.game_won and self.game_started:
            self.win_screen()

        # Rerun the game
        self.run()