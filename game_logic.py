class GameLogic:
    def __init__(self, board_size=3, win_condition=3):
        self.game = TicTacToe(board_size, win_condition)

    def makeMove(self, location, mark):
        return self.game.makeMove(location, mark)

    # Add other game logic methods...
