from tic_tac_toe import TicTacToe
from player import Player, PlayerType

if __name__ == "__main__":
    game = TicTacToe()
    player1 = Player('X', PlayerType.HUMAN)
    player2 = Player('O', PlayerType.RANDOM_AGENT)
    game.setPlayers(player1, player2)

    while not game.isGameOver():
        currentPlayer = game.next()
        move = currentPlayer.makeMove(game.board)
        game.makeMove(move, currentPlayer.letter)
        game.drawBoard()

    winner = game.getWinner()
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")
