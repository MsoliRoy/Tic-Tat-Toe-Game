class TicTacToe:
    def __init__(self, board_size=3, win_condition=3):
        self.board_size = board_size
        self.win_condition = win_condition
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.players = []

    def draw_board(self):
        """Draw the current state of the game board."""
        for row in self.board:
            print("|".join(row))
            print("-" * (self.board_size * 2 - 1))

    def get_key(self, letter):
        """Generate a key representing the state of the board."""
        key = ''
        for row in self.board:
            for cell in row:
                if cell == letter:
                    key += 'L'
                elif cell != ' ':
                    key += 'T'
                else:
                    key += '*'
        return key

    def get_players(self):
        """Get the list of players."""
        return self.players

    def get_winner(self):
        """Check if there's a winner."""
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        for col in range(self.board_size):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None

    def is_game_draw(self):
        """Check if the game is a draw."""
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def is_game_over(self):
        """Check if the game is over."""
        return self.get_winner() is not None or not self.is_game_draw()

    def is_game_won(self, mark):
        """Check if the game is won by a specific player."""
        return self.get_winner() == mark

    def is_same_as(self, char, cell1, cell2, cell3):
        """Check if all provided characters are the same."""
        return cell1 == cell2 == cell3 == char

    def make_move(self, location, mark):
        """Make a move on the board."""
        x, y = location
        if 1 <= x <= self.board_size and 1 <= y <= self.board_size and self.board[x - 1][y - 1] == ' ':
            self.board[x - 1][y - 1] = mark
            return True
        return False

    def next_player(self):
        """Get the next player to make a move."""
        count = sum(row.count(' ') for row in self.board)
        return self.players[count % 2]

    def set_players(self, player1, player2):
        """Set the players for the game."""
        self.players = [player1, player2]


if __name__ == "__main__":
    game = TicTacToe()
    # Play the game
    while not game.is_game_over():
        current_player = game.next_player()
        move = current_player.make_move(game.board)
        game.make_move(move, current_player.letter)
        game.draw_board()

    # Print the result
    winner = game.get_winner()
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a draw!")
