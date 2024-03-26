class GameLogic:
    def __init__(self, game):
        self.game = game

    def make_move(self, location, mark):
        """Make a move on the game."""
        return self.game.make_move(location, mark)

    # Add other game logic methods...

# Example usage:
# Instantiate the TicTacToe game
game = TicTacToe()

# Initialize game logic with the TicTacToe instance
game_logic = GameLogic(game)

# Use game logic to make moves
game_logic.make_move((0, 0), 'X')
