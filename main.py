from tic_tac_toe import TicTacToe
from player import Player, PlayerType


def main():
    """Main function to play Tic Tac Toe game."""
    # Initialize the TicTacToe game
    game = TicTacToe()

    # Create players
    player1 = Player('X', PlayerType.HUMAN)
    player2 = Player('O', PlayerType.RANDOM_AGENT)

    # Set players for the game
    game.set_players(player1, player2)

    # Play the game until it's over
    while not game.is_game_over():
        # Get the current player
        current_player = game.next_player()

        # Make a move
        move = current_player.make_move(game.board)

        # Apply the move to the game board
        game.make_move(move, current_player.letter)

        # Draw the updated game board
        game.draw_board()

    # Print the result
    winner = game.get_winner()
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
