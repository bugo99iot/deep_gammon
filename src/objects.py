from src.parameters import *


class Board(object):
    def __init__(self):
        self.slots = 30
        self.white_pieces_on = 15
        self.black_pieces_on = 15
        self.white_pieces_off = 0
        self.black_pieces_off = 0
        self.white_pieces_safe = 0
        self.black_pieces_safe = 0
        self.state = dict()
        self.state[1] = 2

    def move_piece(self, color, start_location, end_location):
        return 0

    @property
    def game_complete(self):
        if self.white_pieces_safe:
            print("white won")
            return True
        elif self.black_pieces_safe:
            print("back wins")
            return True
        else:
            return False

    def print(self):
        print(self.state)
