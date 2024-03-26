class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.players = []

    # Other methods of TicTacToe class
    # ...
    def drawBoard(self):
        """Draw the current state of the game board."""
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def getKey(self, letter):
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

    def getPlayers(self):
        """Get the list of players."""
        return self.players

    def getWinner(self):
        """Check if there's a winner."""
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        return None

    def isGameDraw(self):
        """Check if the game is a draw."""
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def isGameOver(self):
        """Check if the game is over."""
        return self.getWinner() is not None or self.isGameDraw()

    def isGameWon(self, mark):
        """Check if the game is won by a specific player."""
        return self.getWinner() == mark

    def isSameAs(self, char, a, b, c):
        """Check if all provided characters are the same."""
        return a == b == c == char

    def makeMove(self, location, mark):
        """Make a move on the board."""
        x, y = location
        if 1 <= x <= 3 and 1 <= y <= 3 and self.board[x - 1][y - 1] == ' ':
            self.board[x - 1][y - 1] = mark
            return True
        return False

    def next(self):
        """Get the next player to make a move."""
        count = sum(row.count(' ') for row in self.board)
        return self.players[count % 2]

    def setPlayers(self, player1, player2):
        """Set the players for the game."""
        self.players = [player1, player2]


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
