from constants import BLUE, RED

class Player():
    def __init__(self, color):
        self.color = color
        self.char = 'r' if color == RED else 'b'

        self.pieces = []

        self.score = 0