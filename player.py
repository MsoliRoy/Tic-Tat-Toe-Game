import random
from enum import Enum

class PlayerType(Enum):
    HUMAN = 0
    RANDOM_AGENT = 1

class Player:
    def __init__(self, letter, playerType=PlayerType.HUMAN):
        self.letter = letter
        self.playerType = playerType

    # Other methods of Player class
    # ...

    def makeRandomMove(self, board):
        # Random move logic
        # ...

    def requestMove(self):
        # Human player move logic
        # ...
