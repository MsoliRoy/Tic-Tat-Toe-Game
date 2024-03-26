import random
from enum import Enum

class PlayerType(Enum):
    """Enumeration representing player types."""
    HUMAN = 0
    RANDOM_AGENT = 1

class Player:
    """Class representing a player in the TicTacToe game."""
    
    def __init__(self, letter, playerType=PlayerType.HUMAN):
        """
        Initialize the player.

        Parameters:
        - letter (str): The letter representing the player on the game board.
        - playerType (PlayerType): The type of player (default: PlayerType.HUMAN).
        """
        self.letter = letter
        self.playerType = playerType

    def make_move(self, board):
        """
        Make a move on the board.

        Parameters:
        - board (list): The current state of the game board.

        Returns:
        - int or tuple: The move made by the player.
        """
        if self.playerType == PlayerType.HUMAN:
            return self.request_move()
        elif self.playerType == PlayerType.RANDOM_AGENT:
            return self.make_random_move(board)
        else:
            return None

    def make_random_move(self, board):
        """
        Make a random move on the board.

        Parameters:
        - board (list): The current state of the game board.

        Returns:
        - tuple: The random move made by the player.
        """
        available_moves = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    available_moves.append((i+1, j+1))
        return random.choice(available_moves)

    def request_move(self):
        """
        Request a move from the human player.

        Returns:
        - int: The move entered by the human player.
        """
        while True:
            try:
                move = int(input("Enter move (0-8): "))
                if move < 0 or move > 8:
                    raise ValueError
                return move
            except ValueError:
                print("Invalid move. Please enter a number between 0 and 8.")

# Add TicTacToe class and main game loop here
