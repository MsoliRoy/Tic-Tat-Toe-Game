import random
from enum import Enum

class PlayerType(Enum):
    HUMAN = 0
    RANDOM_AGENT = 1

class Player:
    """Class representing a player in the TicTacToe game."""

    def __init__(self, letter, playerType=PlayerType.HUMAN):
        """Initialize the player."""
        self.letter = letter
        self.playerType = playerType

    def makeMove(self, board):
        """Make a move on the board."""
        if self.playerType == PlayerType.HUMAN:
            return self.requestMove()
        elif self.playerType == PlayerType.RANDOM_AGENT:
            return self.makeRandomMove(board)
        else:
            return None

    def makeRandomMove(self, board):
        """Make a random move on the board."""
        available_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    available_moves.append((i+1, j+1))
        return random.choice(available_moves)

    def requestMove(self):
        """Request a move from the human player."""
        while True:
            try:
                move = int(input("Enter move (0-8): "))
                if move < 0 or move > 8:
                    raise ValueError
                return move
            except ValueError:
                print("Invalid move. Please enter a number between 0 and 8.")
