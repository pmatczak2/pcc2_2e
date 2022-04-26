# tictactoe_oop.py, an object_orianted tic-tac-toe game.

All_SPACES = list('123456789')  # The keys for a TTT board.
X, O, BLANK = 'X', 'O', ' ' # Constant for string values.

def main():
    """Runs game of tic tak toe"""
    print('Welcome to tic tak toe!')
    gameBoard = TTTBoard()  # Creates a TTT board object.
    currentPlayer, nextPlayer = X, O  # X goes first, O goes next.

    while True:
        print(gameBoard.getBoardStr())  # Displays the board on the screen.

        # Keep asking the player until they enter a number 1-9:
        move = None
        while not gameBoard.isValidSpace(move):
            print(f"What is {currentPlayer}\'s move? (1-9)")
            move = input()
        gameBoard.updateBoard(move, currentPlayer)  # Make the move.

        # Check if the game is over.
        if gameBoard.isWinner(currentPlayer):  # Firs check for victory.
            print(currentPlayer + ' has not won the game!')
            break
        elif gameBoard.isBoardFull():   # Next check for a tie.
            print(gameBoard.getBoardStr())
            print('The game is a Tie!')
            break
        currentPlayer, nextPlayer = nextPlayer, currentPlayer  # Swap turns.
        print('Thanks for playing!')

class TTTBoard:
    def __init__(self, usePrettyBoard=False, useLogging=False):
        """Create a new, blank tic tac toe board"""
        self._spaces = {}  # The board is represented as a Python dictionary.
        for space in All_SPACES:
            self._spaces[space] = BLANK  # All spaces start as blank.

    def getBoardStr(self):
        """Return a tect-representation of the board"""
        return f'''
     {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']} 1 2 3
     -+-+
     {self._spaces['4']}|{self._spaces['5']}|{self._spaces['6']} 4 5 6
     -+-+
     {self._spaces['7']}|{self._spaces['8']}|{self._spaces['9']} 7 8 9'''

    def isValidSpace(self, space):
        """Returns True if the space on the board is a valid space numver and the space is blank."""
        return space in All_SPACES and self._spaces[space] == BLANK

    def isWinner(self, player):
        """Return True if player is a winner on this TTTBoard"""
        s, p = self._spaces, player  # Shorter names as "syntactic suger".
        # Check for 3 marks across the 3 rows, 3 columns, and 2 diagonals.
        return ((s['1'] == s['2'] == s['3'] == p) or  # Across the top
                (s['4'] == s['5'] == s['6'] == p) or  # Across the middle
                (s['7'] == s['8'] == s['9'] == p) or  # Across the bottom
                (s['1'] == s['4'] == s['7'] == p) or  # Down the left
                (s['2'] == s['5'] == s['8'] == p) or  # Down the middle
                (s['3'] == s['6'] == s['9'] == p) or  # Down the right
                (s['3'] == s['5'] == s['7'] == p) or  # Diagonal
                (s['1'] == s['5'] == s['9'] == p))    # Diagonal

    def isBoardFull(self):
        """Return True if vevery space on the board gas been taken."""
        for space in All_SPACES:
            if self._spaces[space]  == BLANK:
                return False  # If a single space is blank, return False.
        return True  # No spaces are balnk, so return True.

    def updateBoard(self, space, player):
        """Set the space on the board player."""
        self._spaces[space] = player

if __name__ == "__main__":
    main()