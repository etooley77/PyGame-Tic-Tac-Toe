from random import choice

class Player():
    def __init__(self, color):
        self.color = color

        self.pieces = []

        self.score = 0