class UserInterface:
    def __init__(self, game_logic):
        self.game_logic = game_logic

    def drawBoard(self):
        """Draw the current state of the game board."""
        for row in self.game_logic.game.board:
            print("|".join(row))
            print("-" * 5)

    # Add other user interface methods...
