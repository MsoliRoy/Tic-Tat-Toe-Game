class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = []

    # Other methods of TicTacToe class
    # ...


if __name__ == "__main__":
    game = TicTacToe()
    # Play the game
    while not game.isGameOver():
        currentPlayer = game.next()
        move = currentPlayer.makeMove(game.board)
        game.makeMove(move, currentPlayer.letter)
        game.drawBoard()

    # Print the result
    winner = game.getWinner()
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")
