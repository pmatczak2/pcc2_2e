# tictactoe_oop.py, an object_orianted tic-tac-toe game.

All_SPACES = list('123456789')  # The keys for a TTT board.
X, O, BLANK = 'X', 'B', ' ' # Constant for string values.

def main():
    """Runs game of tic tak toe"""
    print('Welcome to tic tak toe!')
    gameBoard = TTTBoard()  # Creates a TTT board object.
    currentPlayer, nextPlayer = X, O  # X goes first, O goes next.

    while True:
        print(gameBoard.getBoardStr())  # Displays the board on the screen.

        # Keep asking the player until they enter a number 1-9:
        move = None
        while not gameBoard.isValid(move):
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

    def gerBoardStr(self):
        """Return a tect-representation of the board"""
        return f'''
     {self._spaces['1']}|{self._spaces['2']}|{self._spaces['3']}
     -+-+
     '''