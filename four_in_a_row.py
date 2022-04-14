"""A title-dropping game to ger four-in-a-row, similar to Connect Four."""

import sys
# Constant used for displaying the board:
EMPTY_SPACE = "."  # A period is easier to count than a space.
PLAYER_X = "X"
PLAYER_O = "O"

# Note: Update BOARD_TEMPLATE & COLUMN_LABLES if BOARD_WIDTH is changed.
BOARD_WIDTH = 7
BOARD_HEIGHT = 6
COLUMN_LABELS = ("1", "2", "3", "4", "5", "6", "7")
assert len(COLUMN_LABELS) == BOARD_WIDTH

# The template string for display the board:
BOARD_TEMPLATE = """
        1234567
        +-------+
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        |{}{}{}{}{}{}{}|
        +-------+"""

def main():
    """Runs a single game of Four-in-a-row."""
    print(
        """Four-in-a-Row Two players take turns dropping tiles into one of seven clumns, trying
           to make Four-in-a-Row horizontally, vertically, or diagonally. 
           """
    )

    # Set up a new game:
    game_board = getNewBoard()
    playerTurn = PLAYER_X

    while True:  # Run a player's turn.
        # Display the board and get player's move:
        displayBoar(gameBoard)
        playerMove = getplayerMove(playerTurn, gameBoard)
        gameBoard[playerMove] = playerTurn

        # Check for win or tie
        if isWinner(playerTurn, gameBoard):
            displayBoard(gameBoard)  # Display the board one last time.
            print("There is a tie!")
            sys.exit()

        # Switch turns to other player:
        if playerTurn == PLAYER_X:
            playerTurn = PLAYER_O
        elif playerTurn == PLAYER_O:
            playerTurn = PLAYER_X


def getNewBoard():
    """Returns a dicttionary that represents a Four-in-a-Row board.

    The keys are (columnIndex, rowIndex) tuples of two integers, and the values are one of the "X", "O" or "."
    (empty space) strings"""
    board = {}
    for rowIndex in range(BOARD_HEIGHT):
        for cloumnIndex in range(BOARD_WIDTH):
            board[(cloumnIndex, rowIndex)] = EMPTY_SPACE
        return board

    def displayBoard(board):
        """Display the board and its tiles on the screen."""

        # Prepare a list to pass to the format() string method for the board
        # template. THe list holds alll of the board's titles (and empty
        # spaces) going left to right top to bottom:
        titleChars = []
        for rowIndex in range(BOARD_WIDTH):
            titleChars.append(board.[cloumnIndex, rowIndex])

        # Display the board
        print(BOARD_TEMPLATE.format(*titleChars))









